#!/usr/bin/python2 -u
import binascii
import os
import itertools

ROUNDS = 5
BLOCK_LEN = 8
HEX_BLOCK_LEN = BLOCK_LEN * 2
MAX_NOTES = 2048
MAX_NOTE_LEN = 512

def pad(p):
	if len(p) % BLOCK_LEN != 0:
		return p + b"\0" * (BLOCK_LEN - (len(p) % BLOCK_LEN))
	else:
		return p

def g(i):
	b = bin(i).lstrip("0b").rstrip("L").rjust(BLOCK_LEN * 8, "0")
	return int(b[::-1], 2)

def bin_format(i):
	return bin(i).lstrip("0b").rstrip("L").rjust(BLOCK_LEN * 8, "0")

def encrypt_block(b):
	#assert (len(b) * ROUNDS) == len(KEY)
	result = int(binascii.hexlify(b), 16)
	for i in range(ROUNDS):
		#print('\nROUND {}'.format(i+1))
		#print(bin_format(result))
		key = int(binascii.hexlify(KEY[i * BLOCK_LEN:(i + 1) * BLOCK_LEN]), 16)
		key_odd = key | 1
		result ^= key
		#print(bin_format(result))
		result = g(result)
		#print(bin_format(result))
		result = (result * key_odd) % (1 << 64)
		#print(bin_format(result))
	return hex(result).lstrip("0x").rstrip("L").rjust(HEX_BLOCK_LEN, "0")

def encrypt(msg):
	plain = pad(msg)
	result = ""
	for i in range(0, len(plain), BLOCK_LEN):
		result += encrypt_block(plain[i:i + BLOCK_LEN])
	return result

def calc():
	# Setup
	res_diff1 = {}
	res_diff2 = {}

	num_iters = 100000
	for j in range(num_iters):
		# Generate input
		plain = int(binascii.hexlify(os.urandom(8)), 16)

		# Encode plaintext
		plain = binascii.unhexlify(hex(plain).lstrip("0x").rstrip("L").rjust(HEX_BLOCK_LEN, "0"))
		enc = int(binascii.unhexlify(encrypt_block(plain)), 16)

		# Reverse multiplication
		

		# Record lowest bits
		end_diff = int(binascii.hexlify(enc), 16) & 0b111
		if end_diff not in res_diff1:
			res_diff1[end_diff] = 0
		res_diff1[end_diff] += 1

		# Record highest bits
		end_diff = int(binascii.hexlify(enc), 16) & ((1 << 61)+(1 << 62)+(1 << 63)) // (1 << 61)
		if end_diff not in res_diff2:
			res_diff2[end_diff] = 0
		res_diff2[end_diff] += 1

	d1k = sorted(res_diff1, key=res_diff1.get, reverse=True)
	d2k = sorted(res_diff2, key=res_diff2.get, reverse=True)
	print(['{0:03b}: {1:.5f}'.format(i, res_diff1[i]/num_iters) for i in d1k], ['{0:03b}: {1:.5f}'.format(j, res_diff2[j]/num_iters) for j in d2k])

ROUNDS = 5
for i in range(10):
	KEY = os.urandom(40)
	num_key = bin_format(int(binascii.hexlify(KEY), 16))[-64:]
	print(num_key + ' = ', end='')
	calc()