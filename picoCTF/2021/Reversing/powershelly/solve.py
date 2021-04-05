'''
File format:
100011 101011 110111 ...
101101 111011 000110 ...
...

5 lines in total
Each line has exactly 264 blocks, each block is a length 6 binary string
'''

import base64

num_blocks = 264
num_whitespace = num_blocks*5  # 1320, +1 was for carriage return
numLength = num_blocks*6*5+num_whitespace # 9245

# Read correct blocks
with open('correct_out.txt', 'r') as fin:
	correct_res = fin.read().strip().split('\n')
	correct_res = [int(x) for x in correct_res]

# Generate seeds
seeds = []
for i in range(1, num_blocks+1):
	seeds.append(i * 127 % 500)

# Generate random values
randoms = []
for i in range(1, num_blocks+1):
	randoms.append((((i * 327) % 681) + 344) % 313)

# Uncramble function
def unscramble(expected_dbl, seed):
	expected = ''
	for i in range(0, len(expected_dbl), 2):
		expected += expected_dbl[i]
	# print(expected)
	N = len(expected)
	bm = ['10' for _ in range(N)]
	block = ['X' for _ in range(N)]
	for i in range(N):
		# Find the first location to the right of y that is not '10' (looping back to start if needed)
		y = i * seed % N
		while bm[y] != '10':
			y = (y+1) % N
		# Find raw block value based on value at location
		if expected[y] == '1':
			block[i] = '1'
		else:
			block[i] = '0'
		bm[y] = 'XX'
	raw = ''.join(block)
	val = 0
	for i in range(0, N, 6):
		blocks[i//6].append(raw[i:i+6])
		val += int(raw[i:i+6], 2)
	# print(raw)
	# print('unscramble({}, {}) => {}'.format(expected_dbl, seed, raw))
	# vals = b''
	# for i in range(0, N, 6):
	# 	val = bytes([int(raw[i:i+6], 2)])
	# 	vals += val
	# 	blocks[i//6] += val
	# print('unscramble({}, {}) => {}'.format(expected_dbl, seed, raw))

# Calculate input blocks
blocks = [[] for _ in range(5)]
# blocks = [b'' for _ in range(5)]
result = 0
for i in range(num_blocks):
	expected = bin(result ^ randoms[i] ^ correct_res[i])[2:]
	while len(expected) != 60:
		expected = '0' + expected
	# print('unscramble(blocks[{:3d}], {:3d}) => {}'.format(i, seeds[i], expected))
	unscramble(expected, seeds[i])
	result = correct_res[i]


# Write output
with open('correct_in.txt', 'w') as fout:
	for i in range(5):
		for b in blocks[i]:
			if b == blocks[i][0]: fout.write('0')
			else: fout.write('1')
		fout.write('\n')
	# output = b''.join(blocks)
	# fout.write(base64.b64encode(output).decode())
	# fout.write('\n')
