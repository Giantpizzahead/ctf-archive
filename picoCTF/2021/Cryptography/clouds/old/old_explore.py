#!/usr/bin/python2 -u
import binascii
import os
import itertools

ROUNDS = 5
BLOCK_LEN = 8
HEX_BLOCK_LEN = BLOCK_LEN * 2
MAX_NOTES = 2048
MAX_NOTE_LEN = 512
KEY = b'}Y\xeb9\xe2\xefX\xd7\x8f\x19\xa6\xe5\xf9O\xb0\xce\xd2\xa0~\xa4VeY\xdc\xf3\xaf-\xb4\x90\x12\x07\x04\x1d?\xc4\xec\xa9&bv'
KEY = os.urandom(40)

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

def calc_diffs(input_diff):
	# Setup
	res_diff1 = {}
	res_diff2 = {}
	input_diff = int(input_diff, 2)

	num_iters = 10000
	for j in range(num_iters):
		# Generate input with given differential
		plain1 = int(binascii.hexlify(os.urandom(8)), 16)
		plain2 = plain1 ^ input_diff

		# Encode plaintext
		plain1 = binascii.unhexlify(hex(plain1).lstrip("0x").rstrip("L").rjust(HEX_BLOCK_LEN, "0"))
		plain2 = binascii.unhexlify(hex(plain2).lstrip("0x").rstrip("L").rjust(HEX_BLOCK_LEN, "0"))
		enc1 = binascii.unhexlify(encrypt_block(plain1))
		enc2 = binascii.unhexlify(encrypt_block(plain2))

		# Record right bit
		# end_diff = bin_format(int(binascii.hexlify(enc1), 16) ^ int(binascii.hexlify(enc2), 16))
		end_diff = int(binascii.hexlify(enc1), 16) & 0b111
		# end_diff = int(binascii.hexlify(enc1), 16) & 1
		if end_diff not in res_diff1:
			res_diff1[end_diff] = 0
		res_diff1[end_diff] += 1

		# Record left bit
		end_diff = int(binascii.hexlify(enc1), 16) & ((1 << 61)+(1 << 62)+(1 << 63)) // (1 << 61)
		# end_diff = int(binascii.hexlify(enc1), 16) & 1
		if end_diff not in res_diff2:
			res_diff2[end_diff] = 0
		res_diff2[end_diff] += 1

	d1k = sorted(res_diff1, key=res_diff1.get, reverse=True)
	d2k = sorted(res_diff2, key=res_diff2.get, reverse=True)
	print(['{0:03b}: {1:.5f}'.format(i, res_diff1[i]/num_iters) for i in d1k], ['{0:03b}: {1:.5f}'.format(j, res_diff2[j]/num_iters) for j in d2k])

ROUNDS = 5
input_diff = '0'*64

for left_diff in ['000', '100', '111']: #itertools.product('01', repeat=3):
	for right_diff in ['000', '001', '111']: #itertools.product('01', repeat=3):
		left_diff = ''.join(left_diff)
		right_diff = ''.join(right_diff)
		input_diff = left_diff+'0'*58+right_diff
		print(left_diff + ' ' + right_diff + ' = ', end='')
		calc_diffs(input_diff)
