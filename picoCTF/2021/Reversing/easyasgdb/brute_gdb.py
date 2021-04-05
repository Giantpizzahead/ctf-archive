import gdb
import time

# Initial setup
gdb.execute('target exec ./brute')
gdb.execute('break *0x5655590c')
correct_str = '7a2e6e681d65167c6d436f36326212164334403e5801583f623f53306e17'
correct_vals = []
for i in range(0, len(correct_str), 2):
	val = int(correct_str[i:i+2], 16)
	correct_vals.append(val)
flag_len = len(correct_str) // 2

# Brute force the flag
flag = ''
memory_addr = 0x56558c00
while not flag.endswith('}'):
	print('On character {}'.format(len(flag)))

	# First, find which character is affected
	last_output = [-1 for _ in range(flag_len)]
	affected = -1
	for i in range(32, 127):
		exp = flag+chr(i)
		with open('exp', 'w') as fout: fout.write(exp)
		print('Payload:', exp)
		gdb.execute('run < exp')
		# Little endian address

		for j in range(flag_len):
			correct_addr = memory_addr + j
			val = gdb.parse_and_eval('{char}' + str(correct_addr))
			if last_output[j] == -1:
				last_output[j] = val
			elif last_output[j] != val:
				affected = j
				break
		if affected != -1: break

	# Now, find the right character
	possible_chars = []
	for i in range(32, 127):
		exp = flag+chr(i)
		with open('exp', 'w') as fout: fout.write(exp)
		print('Payload:', exp)
		gdb.execute('run < exp')

		correct_addr = memory_addr + affected
		val = gdb.parse_and_eval('{char}' + str(correct_addr))
		# print('Value:', val.address)
		# Is this the right value?
		if val == correct_vals[affected]:
			print('Character {} could be {}'.format(len(flag), chr(i)))
			possible_chars.append(chr(i))
	
	print('Affected:', affected)
	print('Possible:', possible_chars)
	flag += possible_chars[0]

# picoCTF{I_5D3_A11DA7_358a9150}
print('FLAG:', flag)
