# The cipher name is Nimbus! (Hence "Clouds")

import binascii
import itertools
import os
import random
import statistics
from sympy.solvers.diophantine import diophantine
from sympy import symbols
from pwn import *
from Crypto.Util.number import inverse


DEBUG = 0

HOSTNAME = 'mercury.picoctf.net'
PORT = 24402
ROUNDS = 5
BLOCK_LEN = 8
HEX_BLOCK_LEN = BLOCK_LEN * 2
MAX_NOTES = 2048
MAX_NOTE_LEN = 512
# KEYS = [os.urandom(8) for _ in range(ROUNDS)]
PKEYS = [
b'k\xbcBs\xc5F\x10\xc9',
b'\xe1\xfe0\x00Ja\xdd\x05',
b'p\xe3\xc0\xcaS\xf8X\x91',
b'R\x88\x19\xfb\\\x92\xbdE',
b'\t \xdb\xe93\xf2+e'
]
for i in range(ROUNDS): PKEYS[i] = int(binascii.hexlify(PKEYS[i]), 16)

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


'''
Do not call directly.
Pass in an integer to be encrypted, returning an integer.
Must be in range [0, 2^64).
'''
def encrypt_block(b):
	result = b
	for i in range(ROUNDS):
		if DEBUG >= 10:
			print('\nENCRYPT ROUND {}'.format(i+1))
			print(bin_format(result))
		key = PKEYS[i]
		key_odd = key | 1
		result ^= key
		if DEBUG >= 10: print(bin_format(result))
		result = g(result)
		if DEBUG >= 10: print(bin_format(result))
		result = (result * key_odd) % (1 << 64)
		if DEBUG >= 10: print(bin_format(result))
	return result


'''
Pass in an integer to be decrypted, returning an integer.
Must be in range [0, 2^64).
Keys are in reverse order.

KEY 5 ODD: Either 7221599192469485877 or 16444971229324261685
KEY 5: Either 7221599192469485876, 7221599192469485877, 16444971229324261684, or 16444971229324261685
KEY 5: Probably 7221599192469485877

KEY 4 ODD: Either 3617857495015437927 or 12841229531870213735
KEY 4: Either 3617857495015437926, 3617857495015437927, 12841229531870213734, or 12841229531870213735
KEY 4: Probably 3617857495015437926

KEY 3 ODD: Either 7008498656364217669 or 16231870693218993477
KEY 3: Either 7008498656364217668, 7008498656364217669, 16231870693218993476, or 16231870693218993477
KEY 3: Probably 7008498656364217668

KEY 2 ODD: Either 7297316171674891571 or 16520688208529667379
KEY 2: Either 7297316171674891570, 7297316171674891571, 16520688208529667378, or 16520688208529667379

KEY 1 ODD: Either 4990608929225721187 or 14213980966080496995
KEY 1: Either 4990608929225721186, 4990608929225721187, 14213980966080496994, or 14213980966080496995
'''
SELF_ENCRYPT = 5

CKEYS = [
7221599192469485877,
3617857495015437926,
7008498656364217668,
7297316171674891571,
4990608929225721186
]
def decrypt_block(b):
	result = b
	for i in range(ROUNDS):
		if DEBUG >= 10:
			print('\nDECRYPT ROUND {}'.format(i+1))
			print(bin_format(result))
		key = CKEYS[i]
		key_odd = key | 1
		result = (result * pow(key_odd, -1, 1 << 64)) % (1 << 64)
		if DEBUG >= 10: print(bin_format(result))
		result = g(result)
		if DEBUG >= 10: print(bin_format(result))
		result ^= key
		if DEBUG >= 10: print(bin_format(result))
	return result


def test_decrypt():
	for i in range(100):
		x = random.randrange(0, 1 << 64)
		assert(decrypt_block(encrypt_block(x)) == x)
	print('\nDecryption test PASSED')


def decrypt(x_list):
	global ROUNDS
	ROUNDS = SELF_ENCRYPT
	x_list = [decrypt_block(x) for x in x_list]
	ROUNDS = 5
	return x_list


'''
Pass in a list of integers to be encrypted, returning the corresponding list of encrypted integers.
All elements must be in the range [0, 2^64).
'''
conn = None
num_used = 1
MAX_NOTES = 2048
MAX_BLOCKS = 64
def encrypt(x_list, is_remote=False):
	global conn, num_used, ROUNDS
	for x in x_list:
		assert x >= 0 and x < (1 << 64), '{} is not in [0, 2^64)'.format(x)
	# First, encrypt a bit to make the cipher 5 rounds
	ROUNDS = SELF_ENCRYPT
	x_list = [encrypt_block(x) for x in x_list]
	ROUNDS = 5
	# Remote?
	if not is_remote:
		return [encrypt_block(x) for x in x_list]
	else:
		if conn is None: conn = remote(HOSTNAME, PORT)
		dec_res = []
		for i in range(0, len(x_list), MAX_BLOCKS):
			# Send the message in the correct format
			part_list = x_list[i:i+MAX_BLOCKS]
			msg = ''
			for x in part_list:
				part = hex(x)[2:]
				while len(part) < 16: part = '0' + part
				msg += part
			conn.recvuntil('Selection? ')
			conn.sendline('1')
			conn.recvuntil('encrypt: ')
			if DEBUG >= 8: print('Sending', msg)
			conn.sendline(msg)

			# Read the encrypted result
			conn.recvuntil('Selection? ')
			conn.sendline('2')
			conn.recvuntil('read? ')
			conn.sendline(str(num_used))

			# Parse the result and return it
			result = conn.recvline().strip().decode()
			while len(result) > 0:
				part = result[:16]
				dec_res.append(int(part, 16))
				result = result[16:]
			num_used += 1
			if num_used == MAX_NOTES:
				conn.close()
				conn = remote(HOSTNAME, PORT)
				num_used = 1
		if DEBUG >= 8: print('Result:', dec_res)
		return dec_res


'''
Gets the encrypted flag, as a list of blocks.
'''
def get_encrypted_flag():
	global conn
	# Read the encrypted result
	if conn is None: conn = remote(HOSTNAME, PORT)
	conn.recvuntil('Selection? ')
	conn.sendline('2')
	conn.recvuntil('read? ')
	conn.sendline('0')

	# Parse the result and return it
	result = conn.recvline().strip().decode()
	dec_res = []
	while len(result) > 0:
		part = result[:16]
		dec_res.append(int(part, 16))
		result = result[16:]
	if DEBUG >= 8: print('Encrypted flag:', dec_res)
	return dec_res


def apply_differential(a, diff):
	return a * diff % (1 << 64)
	# return (a + diff) % (1 << 64)


def calc_differential(a, b):
	return b * pow(a|1, -1, 1 << 64) % (1 << 64)
	# diff = (b - a) % (1 << 64)
	# if diff < 0: diff += 1 << 64
	# return diff


def test_differential(diff, is_remote=False, num_tests=10000):
	# Generate the blocks
	A = []
	B = []
	for i in range(num_tests):
		a = random.randrange(0, 1 << 64)
		b = apply_differential(a, diff)
		A.append(a)
		B.append(b)
	# Run the test
	enc_A = encrypt(A, is_remote=is_remote)
	enc_B = encrypt(B, is_remote=is_remote)
	res_diff = {}
	for i in range(num_tests):
		new_diff = calc_differential(enc_A[i], enc_B[i])
		if new_diff not in res_diff:
			res_diff[new_diff] = 0
		res_diff[new_diff] += 1
	res_items = sorted(res_diff.items(), key=lambda item: item[1])
	if DEBUG >= 5 or (DEBUG >= 3 and res_items[0][1] != res_items[-1][1]):
		print('\n----- Differential of {} -----'.format(bin_format(diff)))
		to_print = 3
		print('Maximum probability:')
		for i in range(-1, max(-(to_print+1), -len(res_items))-1, -1):
			print('{:7d} | {}'.format(res_items[i][1], bin_format(res_items[i][0])))
		print('Minimum probability:')
		for i in range(min(to_print-1, len(res_items)-1), -1, -1):
			print('{:7d} | {}'.format(res_items[i][1], bin_format(res_items[i][0])))
		if len(res_items) > 1:
			print('Standard deviation: {:.5f}'.format(statistics.stdev([item[1] for item in res_items])))
	elif DEBUG >= 4:
		print('No bias found: Differential of {}'.format(bin_format(diff)))
	return res_items


'''
https://link.springer.com/content/pdf/10.1007%2F3-540-45473-X_16.pdf
'''
KEYS = [[] for _ in range(5)]
KEYS_ODD = [[] for _ in range(5)]
NUM_PAIRS = 64


def find_matching(enc):
	matching = []
	corr_bit = 0
	for i in range(NUM_PAIRS):
		A = enc[0][i]
		B = enc[1][i]
		if (A ^ B) & 0b11 != 0b10: continue  # Criteria 1
		if A & 1 != 0 or B & 1 != 0: continue  # Criteria 2
		matching.append([A, B])
		if (A ^ B) & 0b100 == 0: corr_bit -= 1
		else: corr_bit += 1
	if corr_bit > 0: print('3rd LSB is 1 [{}]'.format(corr_bit))
	elif corr_bit < 0: print('3rd LSB is 0 [{}]'.format(corr_bit))
	else: print('Same chance for 3rd LSB, assuming 0')
	# Criteria 3
	i = 0
	while i < len(matching):
		if (corr_bit > 0) == ((matching[i][0] ^ matching[i][1]) & 0b100 == 0):
			matching.pop(i)
			i -= 1
		i += 1
	return matching


'''
def first_k_bits(n, k):
	return n % (1 << k)

def recover_two_ks(pairs, diff):
	k0 = 1; k0b = 1
	k1 = pairs[0][0] & 1; k1b = 1
	a0 = 0; a0b = 1
	b0 = 0; b0b = 1
	c0 = pairs[0][0]
	d0 = pairs[0][1]
	Z = 0
	while True:
		xor = c0 ^ d0
		next_k0 = 1 ^ (xor & (1<<(Z+2) != 0))
		k0 += 1 << (Z+1); k0b += 1
		if next_k0 == 1:
			# Cannot find any more
			break
		else:
			# Keep going
			Z += 1
	# Start guessing
	print()
	print('k0', bin(k0), k0b)
	print('k1', bin(k1), k1b)
	print('a0', bin(a0), a0b)
	print('b0', bin(b0), b0b)
	while True:
		s_diff = first_k_bits(diff, a0b+3)
		multbits = min(a0b+3, k0b+2)
		s_c0 = first_k_bits(c0, multbits)
		s_d0 = first_k_bits(d0, multbits)
		for guess_a0 in range(8):
			for guess_k0 in range(4):
				# Modify for guess
				a0 += guess_a0 << a0b; a0b += 3
				k0 += guess_k0 << k0b; k0b += 2
				b0 = a0 ^ s_diff; b0b = a0b
				multa = a0*k0
				multb = b0*k0
				print('Guess', bin(a0), bin(b0), bin(k0), bin(s_c0), bin(s_d0))
				print('XOR', bin(first_k_bits(multa ^ multb, multbits)), bin(s_c0 ^ s_d0))
				if first_k_bits(multa ^ multb, multbits) == s_c0 ^ s_d0:
					# Check this guess further
					k1 = s_c0 ^ (a0*k0)
					m, n = symbols("m, n", integer=True)
					for p in pairs:
						ci = first_k_bits(p[0], multbits)
						C = ci ^ k1
						ai = diophantine(n*k0 - C + m*(1<<multbits))
						print(ai)
						ai = int(ai.pop()[1] % (1<<multbits))
						print('({} * {}) ^ {} = {}'.format(bin(ai), bin(k0), bin(k1), bin(ci)))
						assert first_k_bits((ai*k0) ^ k1, multbits) == ci, 'Recover equations sol wrong'
				# Backtrack
				a0b -= 3; a0 -= guess_a0 << a0b
				k0b -= 2; k0 -= guess_k0 << k0b
				b0 = a0 ^ s_diff; b0b = a0b
		break

	print()
	print('k0', bin(k0), k0b)
	print('k1', bin(k1), k1b)
	print('a0', bin(a0), a0b)
	print('b0', bin(b0), b0b)
'''



def find_key5_odd():
	random.seed(time.time())
	print('Generating / encrypting plaintext pairs...')
	diff = int('0'+'1'*62+'0', 2)
	# plain[0] = Normal, plain[1] = Most sig, plain[2] = Least sig, plain[3] = Most and least sig
	plain = [[[], []], [[], []], [[], []], [[], []]]
	# Part 1
	for i in range(NUM_PAIRS):
		a = random.randrange(0, 1 << 64) & diff
		b = a ^ diff
		plain[0][0].append(a)
		plain[0][1].append(b)
		plain[1][0].append(a|(1<<63))
		plain[1][1].append(b|(1<<63))
		plain[2][0].append(a|1)
		plain[2][1].append(b|1)
		plain[3][0].append(a|1|(1<<63))
		plain[3][1].append(b|1|(1<<63))
	enc = [[], [], [], []]
	for i in range(4):
		for j in range(2):
			enc[i].append(decrypt(encrypt(plain[i][j], is_remote=True)))
	# for i in range(4):
	# 	for j in range(2):
	# 		print([bin_format(p) for p in enc[i][j]])

	# Find the delta structure
	delta_struct = 0
	max_diff = 0
	for i in range(4):
		has_diff = 0
		for j in range(NUM_PAIRS):
			if enc[i][0][j] ^ enc[i][1][j] == diff:
				has_diff += 1
		if has_diff > max_diff:
			delta_struct = i
			max_diff = has_diff
		print('Structure {} has_diff = {}'.format(i, has_diff))
	print('Taking structure {} as delta structure'.format(delta_struct))

	# Find matching pairs
	matching = find_matching(enc[delta_struct])
	print('Matching pairs:', len(matching))

	# Solve equation (diff * K' = C_1 + C_2)
	k5_odd = {}
	for p in matching:
		m, n = symbols("m, n", integer=True)
		ans = int(diophantine(diff * n - p[0] - p[1] + (1<<64) * m).pop()[1] % (1 << 63))
		# print('{} * K = {} + {}, so K = {}'.format(diff, p[0], p[1], ans))
		assert diff * ans % (1 << 64) == (p[0] + p[1]) % (1 << 64), 'Equation sol incorrect'
		if ans not in k5_odd:
			k5_odd[ans] = 0
		k5_odd[ans] += 1
	# print(k5_odd)
	most_common = -1
	most_times = 0
	for k in k5_odd.keys():
		if k5_odd[k] > most_times:
			most_times = k5_odd[k]
			most_common = k
	print('KEY {} ODD: Either {} or {}'.format(ROUNDS-SELF_ENCRYPT, most_common, most_common|(1<<63)))

	'''
	# Partially decrypt values
	part_decrypted = [[], []]
	for i in range(NUM_PAIRS):
		A = enc[delta_struct][0][i]
		A = (A * pow(KEYS_ODD[4][0], -1, 1 << 64)) % (1 << 64)
		B = enc[delta_struct][1][i]
		B = (B * pow(KEYS_ODD[4][0], -1, 1 << 64)) % (1 << 64)
		part_decrypted[0].append(A)
		part_decrypted[1].append(B)

	# Find matching pairs
	matching = find_matching(part_decrypted)
	print('Num matching: {}'.format(len(matching)))
	# print('Matching pairs:', matching)
	while True:
		result = recover_two_ks(random.sample(matching, 4), diff)
		print(result)
		input()
	'''


def main():
	flag_arr = decrypt(get_encrypted_flag())
	flag_arr = ''.join([hex(p)[2:] for p in flag_arr])
	flag = binascii.unhexlify(flag_arr)
	print(flag)
	find_key5_odd()
	'''
	print(encrypt([i for i in range(64)], is_remote=False))
	print(encrypt([i%73 for i in range(60000)], is_remote=True))
	print(get_encrypted_flag())
	'''


if __name__ == '__main__':
	main()
