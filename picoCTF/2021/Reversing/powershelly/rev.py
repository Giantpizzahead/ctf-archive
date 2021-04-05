'''
File format:
100011 101011 110111 ...
101101 111011 000110 ...
...

5 lines in total
Each line has exactly 264 blocks, each block is a length 6 binary string
'''

num_blocks = 264
num_whitespace = num_blocks*5  # 1320, +1 was for carriage return
numLength = num_blocks*6*5+num_whitespace # 9240

# Read input
with open('input.txt', 'r') as fin:
	data = fin.read().strip()

with open('correct_out.txt', 'r') as fin:
	correct_res = fin.read().strip().split('\n')
	correct_res = [int(x) for x in correct_res]

# Sanity checks
# assert len(data.split('\n')) <= 5, 'Too many lines'
# assert len(data) == numLength, 'Wrong length'
# for c in data:
# 	assert c in '01\n\r ', 'Invalid character {}'.format(c)
data = data.split('\n')
data = [x.strip() for x in data]
num_blocks = len(data[0].split(' '))

# Split input into 6-character blocks
blocks = [[] for _ in range(num_blocks)]
for i in range(len(data)):
	r = data[i].split(' ')
	for j in range(len(r)):
		assert len(r[j]) == 6, 'Invalid binary string length'
		blocks[j].append(r[j])

# Generate seeds
seeds = []
for i in range(1, num_blocks+1):
	seeds.append(i * 127 % 500)

# Generate random values
randoms = []
for i in range(1, num_blocks+1):
	randoms.append((((i * 327) % 681) + 344) % 313)

# Scramble function
def scramble(block, seed):
	raw = ''.join(block)
	N = len(raw)
	bm = ['10' for _ in range(N)]
	for i in range(N):
		# Find the first location to the right of y that is not '10' (looping back to start if needed)
		y = i * seed % N
		x = bm[y]
		while x != '10':
			y = (y+1) % N
			x = bm[y]
		# Sets that location to either 11 or 00, depending on the raw block
		if raw[i] == '1':
			x = '11'
		else:
			x = '00'
		bm[y] = x
	raw2 = ''.join(bm)
	# print('scramble({}, {}) => {}'.format(block, seed, raw2))
	return int(raw2, 2)

# Calculate final blocks
output = []
result = 0
for i in range(num_blocks):
	# Correctness check
	# expected = correct_res[i]
	# print('scramble(blocks[{:3d}], {:3d}) => {}'.format(i, seeds[i], bin(result ^ randoms[i] ^ expected)[2:]))
	# Update result
	enc = scramble(blocks[i], seeds[i])
	result = result ^ enc ^ randoms[i]
	output.append(result)
	# Make sure result is set
	# result = expected


# Write output
with open('output.txt', 'w') as fout:
	fout.write('\n'.join([str(x) for x in output]))
	fout.write('\n')
