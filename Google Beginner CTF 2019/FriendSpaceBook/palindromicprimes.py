from itertools import chain
import math

def isprime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0: return False
    return True

limit = 10**4

seq = sorted((n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1, limit)), (int(str(x)+str(x)[-2::-1]) for x in range(1, limit))) if isprime(n)))

print(seq[99])
