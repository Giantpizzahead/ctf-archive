import gmpy2

# Predict Merseene Twister values
inp_out_xor_bitsY = [
	0xfe87caa8,
	0x400091,
	0x84092000,
	0x1000044,
	0x2040489,
	0x6000990,
	0x8001220,
	0xeea7cea0,
	0x20004880,
	0x4080002,
	0x80002200,
	0xff95eeac,
	0x2000880,
	0x8081202,
	0x10102404,
	0x204008,
	0x44089102,
	0x84892122,
	0xff85cae8,
	0x2440010,
	0x84012002,
	0x1100040,
	0xecb3ea6d,
	0x6400980,
	0xc881302,
	0x6fa7eee0,
	0x22004800,
	0x80102,
	0x88002000,
	0xef95eaac,
	0x22000080,
	0xc001300
]

def gen_new_2(MT_623, MT_227):
	r = 0
	i = 0
	while True:
		r ^= (MT_623 & 1) * inp_out_xor_bitsY[i]
		i += 1
		MT_623 //= 2
		if MT_623 == 0: break
	r ^= MT_227
	return (r, r^0x44081102)

def gen_new_3(MT_624, MT_623, MT_227):
	r = 0
	i = 0
	while True:
		r ^= (MT_623 & 1) * inp_out_xor_bitsY[i]
		i += 1
		MT_623 //= 2
		if MT_623 == 0: break

	MT_624 &= 0x89130204;
	MT_624 ^= MT_624 >> 16;
	MT_624 ^= MT_624 >> 8;
	MT_624 ^= MT_624 >> 4;
	MT_624 ^= MT_624 >> 2;
	MT_624 ^= MT_624 >> 1;
	r ^= (MT_624 & 1) * 0x44081102;
	r ^= MT_227
	return r

def gen_new_3_227(MT_624, MT_623, MT_0):
	r = 0
	i = 0
	while True:
		r ^= (MT_623 & 1) * inp_out_xor_bitsY[i]
		i += 1
		MT_623 //= 2
		if MT_623 == 0: break

	MT_624 &= 0x89130204;
	MT_624 ^= MT_624 >> 16;
	MT_624 ^= MT_624 >> 8;
	MT_624 ^= MT_624 >> 4;
	MT_624 ^= MT_624 >> 2;
	MT_624 ^= MT_624 >> 1;
	r ^= (MT_624 & 1) * 0x44081102;
	r ^= MT_0
	return r

def predict(MT_623, MT_227, MT_0):
	x = gen_new_2(MT_623, MT_227)
	if MT_0 == -1:
		return x
	else: return MT_0 == x[0] or MT_0 == x[1]

# ----------- Main code -----------

B = []
Y = []

with open('keydata.txt', 'r') as fin:
	while True:
		line = fin.readline()
		if not line: break
		line = line.split()
		new_bits = [-1 for _ in range(2048 // 32)]
		if line[0] == 'private':
			# Known bits
			p = int(line[1])
			for i in range(1024 // 32):
				new_bits[i] = p % (2 ** 32)
				p //= (2 ** 32)
			q = int(line[2])
			for i in range(1024 // 32):
				new_bits[1024 // 32 + i] = q % (2 ** 32)
				q //= (2 ** 32)
		B += new_bits

N = len(B)
Y = [False for _ in range(N)]

def fill_for_sure():
	num_filled = 0
	for i in range(N):
		# Predict this bit if possible (definitely correct)
		x = -1
		if i >= 624 and Y[i-624] and Y[i-623] and Y[i-227]:
			x = gen_new_3(B[i-624], B[i-623], B[i-227])
		elif i >= (624-227) and i < N-227 and Y[i-(624-227)] and Y[i-(623-227)] and Y[i+227]:
			x = gen_new_3_227(B[i-(624-227)], B[i-(623-227)], B[i+227])
		else:
			continue
		Y[i] = True
		if B[i] != x:
			B[i] = x
			num_filled += 1
	return num_filled

def fill_bits(B):
	num_types = {'f': 0, 'c': 0, 'X': 0}
	for i in range(N):
		if i >= 624 and B[i-624] != -1 and B[i-623] != -1 and B[i-227] != -1:
			# Predict this bit
			x = gen_new_3(B[i-624], B[i-623], B[i-227])
			if B[i] == -1:
				B[i] = x
				num_types['f'] += 1
				# print('f', end='')
			elif B[i] == x:
				num_types['c'] += 1
				# print('c', end='')
			else:
				num_types['X'] += 1
				# print('X', i, end='')
	return num_types['X']

'''
# Fix current bits by simulating and taking the best outcome
for i in range(N):
	if i % 32 > 1 or B[i] == -1: continue  # Unlikely to be wrong
	best_j = 0
	best_wrong = N
	for j in range(10000):
		new_B = B[:]
		new_B[i] -= j
		wrong = fill_bits(new_B)
		if wrong < best_wrong:
			best_wrong = wrong
			best_j = j

	print('Index {}: -{} ({} wrong)'.format(i, best_j, best_wrong))
	B[i] -= best_j

# Fix current bits
num_fixed = 0
for i in range(N):
	if i >= 624 and B[i-623] != -1 and B[i-227] != -1 and B[i] != -1:
		x = predict(B[i-623], B[i-227], B[i])
		if not x:
			# The value with index % 32 close to 0 is likely the wrong one (less significant int)
			num_tries = 10000
			fixed = False
			real_ind = [623, 227, 0]
			arr = [B[i-623], B[i-227], B[i]]
			fixes = []
			# Try single
			for k in range(3):
				if (i-real_ind[k]) % 32 > 1: continue
				for j in range(1, num_tries):
					arr[k] -= j
					x = predict(*arr)
					if x:
						fixes.append((k, j))
						# B[i-real_ind[k]] -= j
						# fixed = True
					arr[k] += j
			if fixes:
				print(fixes[:5], end=": ")
				# Try the fix with the smallest adjustment
				best = fixes[0]
				for fix in fixes:
					if fix[1] < best[1]: best = fix
				print((i-real_ind[best[0]], -best[1]))
				B[i-real_ind[best[0]]] -= best[1]
				fixed = True
			if fixed:
				num_fixed += 1
				print('fixed', i)
			else:
				print('cannot fix', i)
print('# fixed:', num_fixed)
'''

# Anything with i % 32 > 1 should be correct
for i in range(N):
	if B[i] != -1 and i % 32 > 1: Y[i] = True
num_filled = 1
while num_filled:
	num_filled = fill_for_sure()
for i in range(N):
	if not Y[i]: B[i] = -1

# Check final tally
print('\nfinal tally')
num_types = {'f': 0, 'c': 0, 'X': 0}
wrong_locs = []
for i in range(N):
	if i >= 624 and B[i-624] != -1 and B[i-623] != -1 and B[i-227] != -1:
		# if not (Y[i-624] and Y[i-623] and Y[i-227]):
		# 	print('?', end='')
		# 	continue
		# Predict this bit
		x = gen_new_3(B[i-624], B[i-623], B[i-227])
		if B[i] == -1:
			B[i] = x
			num_types['f'] += 1
			print('f', end='')
		elif B[i] == x:
			num_types['c'] += 1
			print('c', end='')
		else:
			wrong_locs.append(i)
			num_types['X'] += 1
			print('X', end='')
	else:
		print('-', end='')
print('\nwrong:', wrong_locs)
print(num_types)

with open('randbits.txt', 'w') as fout:
	fout.write(repr(B))