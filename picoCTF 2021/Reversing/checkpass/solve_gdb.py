import gdb
import time

# Initial setup
BASE_ADDR = 0x555555554000
gdb.execute('target exec ./checkpass')

# Set all breakpoints
step_locs = [0x5d1b, 0x5d48, 0x5d77, 0x5da6, 0x5dd5, 0x5e02, 0x5e2e, 0x5e5b,
			 0x5e88, 0x5eb5, 0x5ee2, 0x5f12, 0x5f42, 0x5f72, 0x5fa2, 0x5fd2,
			 0x6002, 0x6032, 0x6062, 0x6092, 0x60c2, 0x60f2, 0x6122, 0x6152,
			 0x6182, 0x61b2, 0x61e2, 0x6212, 0x6242, 0x6272, 0x629e, 0x66a0]
bad_locs = [0x356a0, 0x32f80, 0x34220, 0x6650, 0x1f1d0] # 0x6600 invalid len
for loc in step_locs:
	gdb.execute('break *{}'.format(BASE_ADDR + loc))
for loc in bad_locs:
	gdb.execute('break *{}'.format(BASE_ADDR + loc))

# Execute the program, counting the number of step locs it reaches
def count_steps(exp):
	gdb.execute('run "{}"'.format(exp), to_string=True)
	# Check breakpoints
	num_steps = 0
	while True:
		loc = int(gdb.parse_and_eval('$rip')) - BASE_ADDR
		if loc in step_locs:
			num_steps += 1
			gdb.execute('continue')
		elif loc in bad_locs:
			print('Payload: {} [{}]'.format(exp, num_steps))
			return num_steps
		else:
			raise Exception('{} not found in lists!'.format(hex(loc)))


# Brute force the flag
flag = [' ' for _ in range(32)]
char_set = [False for _ in range(32)]
blacklist = '"`}{\\$'
step_count = 0
while step_count < 32:
	print('On step count {}'.format(step_count))

	# Try changing all unset characters to this value
	best_k = []
	best_steps = step_count
	for k in range(32, 127):
		if chr(k) in blacklist: continue
		exp = flag[:]
		for j in range(32):
			if char_set[j]: continue
			exp[j] = chr(k)
		exp = 'picoCTF{' + ''.join(exp) + '}'
		steps = count_steps(exp)
		if steps > best_steps:
			best_k = []
			best_steps = steps
		if steps == best_steps:
			best_k.append(k)
	print('best_k:', best_k)
	print('best_steps:', best_steps)
	best_k = best_k[0]

	# Find which unset character to change
	best_j = []
	best_steps = step_count
	for j in range(32):
		if char_set[j]: continue
		exp = flag[:]
		exp[j] = chr(best_k)
		exp = 'picoCTF{' + ''.join(exp) + '}'
		steps = count_steps(exp)
		if steps > best_steps:
			best_j = []
			best_steps = steps
		if steps == best_steps:
			best_j.append(j)
	print('best_j:', best_j)
	print('best_steps:', best_steps)
	best_j = best_j[0]

	# Fix the found character
	print('Setting character {} to {}'.format(best_j, chr(best_k)))
	flag[best_j] = chr(best_k)
	char_set[best_j] = True
	step_count = best_steps

# picoCTF{t1mingS1deChann3l_gVQSfJxl3VPFGQ}
print('FLAG:', 'picoCTF{' + ''.join(flag) + '}')
