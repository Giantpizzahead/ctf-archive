# https://mathoverflow.net/questions/120160/attack-on-crt-rsa
# Use a divide and conquer approach to make this run fast enough

import random
import os
import sys
import math
import sympy
import time
import numpy as np
from sympy import ntt, intt
from multiprocessing import Pool
from Crypto.Util.number import GCD

if len(sys.argv) > 1:
	N = int(sys.argv[1])
	e = int(sys.argv[2])
	D = int(sys.argv[3])
else:
	N = 146975320698968190565260106200986271117791009112255997487643711870003600883598081268834485671406368075450281421876928838726135489974359610326517044525392544406121326263646260642144986158197747452314042513847441471427278473430133421087724861363391895180988655815339130711119816187042544490030427453604399237087
	e = 110563215138182921582247642823132153337807436027737934674243095447014135875354168058750848092298825348678116416335449514132138553459693795368409864803141268322041304320938396438515077223451462124135613666158244709032745966050270742099026079913193967975174140288912929767526234658221624847704224697255226248653
	D = 1 << 10
# print('N:', N)
# print('e:', e)
# print('D:', D)

timeout = 840
x = random.randint(1, N-1)

'''
for m in range(200):
	for k in range(1000, 1300):
		num = m*2**k + 1
		if sympy.ntheory.isprime(num):
			print("{}*2**{}+1".format(m, k))

# ntt_prime = 3*2**8+1
ntt_prime = 27*2**1076+1
def poly_mult(A, B):
	L = len(A)+len(B)
	while len(A) < L: A.append(0)
	while len(B) < L: B.append(0)
	A_f = ntt(A, ntt_prime)
	B_f = ntt(B, ntt_prime)
	C_f = [0 for _ in range(len(A_f))]
	for i in range(len(C_f)):
		C_f[i] = A_f[i] * B_f[i] % ntt_prime
	C = intt(C_f, ntt_prime)
	for i in range(len(C)):
		C[i] %= N
	print(A, '*', B, '=', C)
	return C

# Compute the polynomial
poly = [1, 0]
curr_x = 1
chg_x = pow(x, e, N)
for i in range(D):
	poly2 = [-x+N, curr_x]
	poly = poly_mult(poly, poly2)
	curr_x = curr_x * chg_x % N

# Evaluate the polynomial
'''

# Compute the parts of the polynomial
print('\nComputing polynomial parts')
polys = []
curr_x = 1
chg_x = pow(x, e, N)
for i in range(D):
	polys.append([-x+N, curr_x])
	curr_x = curr_x * chg_x % N

# Compute points to evaluate the polynomial at
print('\nComputing evaluation points')
y_vals = []
curr_y = 1
chg_y = pow(x, e*D, N)
for b in range(D):
	y_vals.append(curr_y)
	curr_y = curr_y * chg_y % N

'''
# Multiply polynomial using divide and conquer
def poly_mult(p, q):
	n = len(p)
	m = (n+1)//2
	if n == 1:
		return [p[0]*q[0]%N]
	else:
		a = p[m:n]
		b = p[0:m]
		c = q[m:n]
		d = q[0:m]
		tmp2 = poly_mult(a, c)
		tmp3 = poly_mult(b, d)
		for i in range(len(a)):
			b[i] += a[i]
		for i in range(len(c)):
			d[i] += c[i]
		tmp1 = poly_mult(b, d)
		r = [0 for _ in range(2*n)]
		for i in range(len(tmp1)):
			r[m+i] += tmp1[i]
		for i in range(len(tmp2)):
			r[n+i] += tmp2[i]
			r[m+i] -= tmp2[i]
		for i in range(len(tmp3)):
			r[i] += tmp3[i]
			r[m+i] -= tmp3[i]
		for i in range(len(r)):
			r[i] %= N
			if r[i] < 0: r[i] += N
		return r

# Divide and conquer
calls = 0
total_calls = D*2-1
next_progress = 0
def dac(l, r):
	global calls, next_progress
	# Update progress
	calls += 1
	if calls*100 // total_calls > next_progress:
		next_progress = calls*100 // total_calls
		print('Progress: {}%'.format(next_progress))
	if l == r: return polys[l]
	m = (l+r)//2
	return poly_mult(dac(l, m), dac(m+1, r))

print('\nMultiplying polynomial...')
poly = dac(0, D-1)


# Divide and conquer
calls = 0
total_calls = D*2-1
next_progress = 0
res = [0 for _ in range(D)]
def dac(l, r):
	global calls, next_progress
	# Update progress
	calls += 1
	if calls*100 // total_calls > next_progress:
		next_progress = calls*100 // total_calls
		print('Progress: {}%'.format(next_progress))
	if l > r:
		# Empty
		pass
	elif l == r:
		# Only one polynomial
		for i in range(D):
			res[i] = (polys[l][0] + polys[l][1] * y_vals[i]) % N
	else:
		# Recurse and combine results
		m = (l+r)//2
		res_left = dac(l, m)[:]
		res_right = dac(m+1, r)
		for i in range(D):
			res[i] = res_left[i] * res_right[i] % N
	return res

print('\nDividing and conquering')
res = dac(0, D-1)
'''

def eval_num(b):
	# print('Eval {}'.format(b))
	y = y_vals[b]
	R = 1
	for poly in polys:
		R = (poly[0] + poly[1] * y) % N * R % N
	gcd = GCD(R, N)
	if gcd != 1:
		# os.system('spd-say "A result has been found hello hello yay yay please check quick ok thanks bye bye now"')
		# print('Pos {}, value {} = GCD {}'.format(b, R, gcd))
		# print()
		P = gcd
		Q = N // gcd
		print(P)
		print(Q)
		print(P+Q)


mp = Pool()
# print('\nEvaluating + Finding GCDs')
# os.system('spd-say "Here we go!"')
nums = [b for b in range(D)]
random.shuffle(nums)
async_res = mp.map_async(eval_num, nums)

# Wait until time limit has passed, then end and give up
start_time = time.time()
while True:
	if async_res.ready() or time.time() - start_time > timeout:
		# Everything is done
		break
	time.sleep(5)

'''
def eval_num(b):
	# print('Eval {}'.format(b))
	curr_y = 1
	y = y_vals[b]
	R = 0
	for coeff in poly:
		R = (R + coeff * curr_y) % N
		curr_y = y * curr_y % N
	gcd = GCD(R, N)
	if gcd != 1:
		# os.system('spd-say "A result has been found hello hello yay yay please check quick ok thanks bye bye now"')
		# print('Pos {}, value {} = GCD {}'.format(b, R, gcd))
		# print()
		P = gcd
		Q = N // gcd
		print(P)
		print(Q)
		print(P+Q)

mp = Pool()
print('\nEvaluating + Finding GCDs')
os.system('spd-say "Here we go!"')
nums = [b for b in range(D)]
random.shuffle(nums)
async_res = mp.map_async(eval_num, nums)

# Wait until time limit has passed, then end and give up
start_time = time.time()
while True:
	if async_res.ready() or time.time() - start_time > timeout:
		# Everything is done
		break
	time.sleep(5)
'''
