#!/usr/bin/python3 -u
'''
d * e % tot(n) = 2
d * e % (p-1) = 2
d * e % (q-1) = 2


d * e % (p-1)
d % (p-1) = d_p
d % (q-1) = d_q
d = 
'''

import random
import string
import hashlib
import time

from Crypto.Util.number import inverse, getPrime, bytes_to_long, GCD
from sympy.ntheory.modular import solve_congruence

FLAG = open('flag.txt', 'r').read()

def CRT(a, m, b, n):
	val, mod = solve_congruence((a, m), (b, n))
	return val

def gen_key():
	while True:
		p = getPrime(512//32)
		q = getPrime(512//32)
		if GCD(p-1, q-1) == 2:
			return p, q

def get_clue(p, q, BITS):
	while True:
		d_p = random.randint(1, 1 << BITS)  # [1, 2^20]
		d_q = random.randint(1, q - 1)      # [1, q-1]
		if d_p % 2 == d_q % 2:
			print("d_p:", d_p)
			print("d_q:", d_q)
			# Finds d such that d % (p-1) = d_p and d % (q-1) = d_q
			d = CRT(d_p, p - 1, d_q, q - 1)
			print("d:", d)
			# Finds modular inverse of d
			e = inverse(d, (p - 1) * (q - 1))
			print("Clue : ", e)
			return

def get_flag(p, q):
	start = time.time()
	ans = int(input())
	if (time.time() - start) > (15 * 60):
		print("Too long!")
		exit()
	else:
		if ans == p + q:
			print(FLAG)
		else:
			print("oops...")


#PoW

p, q = gen_key()
n = p * q
print("Public Modulus : ", n)
get_clue(p, q, 20-15)
print("p:", p)
print("q:", q)
get_flag(p, q)
