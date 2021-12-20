#!/usr/bin/python3 -u
import random
import string
import hashlib
import time

from Crypto.Util.number import inverse, getPrime, bytes_to_long, GCD
from sympy.ntheory.modular import solve_congruence

FLAG = open('flag.txt', 'r').read()

def CRT(a, m, b, n):
	val, mod = solve_congruence((a, m), (b, n))
	print("\nCRT({}, {}, {}, {}) => ({}, {})".format(a, m, b, n, val, mod))
	return val

def gen_key():
	while True:
		p = getPrime(512)
		q = getPrime(512)
		# p = getPrime(64)
		# q = getPrime(512)
		if GCD(p-1, q-1) == 2:
			return p, q

def get_clue(p, q, BITS):
	while True:
		d_p = random.randint(1, 1 << BITS)
		d_q = random.randint(1, q - 1)
		# d_p = random.randint(1, p - 1)
		# d_q = random.randint(1, 1 << BITS)
		if d_p % 2 == d_q % 2:
			d = CRT(d_p, p - 1, d_q, q - 1)
			e = inverse(d, (p - 1) * (q - 1))
			remainder = d*e % ((p-1)*(q-1))
			if remainder != 1:
				print("[EDGE CASE] remainder = {}".format(remainder))
			print("\ne: ", e)
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
print("\nN: ", n)
get_clue(p, q, 20)
# get_clue(p, q, 20)
# Debug info
print("\np: ", p)
print("\nq: ", q)
get_flag(p, q)
