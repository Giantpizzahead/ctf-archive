'''
Created on Dec 14, 2011

@author: pablocelayes
'''

import ContinuedFractions, Arithmetic, RSAvulnerableKeyGenerator

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

# TEST functions

def test_hack_RSA():
    print("Testing Wiener Attack")
    times = 5
    
    while(times>0):
        e,n,d = RSAvulnerableKeyGenerator.generateKeys(1024)
        print("(e,n) is (", e, ", ", n, ")")
        print("d = ", d)
    
        hacked_d = hack_RSA(e, n)
    
        if d == hacked_d:
            print("Hack WORKED!")
        else:
            print("Hack FAILED")
        
        print("d = ", d, ", hacked_d = ", hacked_d)
        print("-------------------------")
        times -= 1

arr_n = []
arr_e = []
with open('publickeys.txt', 'r') as fin:
    while True:
        a = fin.readline()
        b = fin.readline()
        fin.readline()
        if a:
            n = int(a.split()[2], 16)
            e = int(b.split()[2], 16)
            arr_n.append(n)
            arr_e.append(e)
        else:
            break

# MetaCTF{Oops_those_primes_are_not_that_randoM}

for i in range(len(arr_n)):
    d = hack_RSA(arr_e[i], arr_n[i])
    if d:
        print(bytearray.fromhex(hex(d)[2:]).decode())
        print(i, 'crack')
