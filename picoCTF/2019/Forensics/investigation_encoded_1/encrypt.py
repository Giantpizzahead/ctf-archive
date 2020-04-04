"""
Max supported file size is 65535

buffChar = 0
remain = 7			

getValue(c)


lower(c) - Returns lowercase version of a letter. Space doesn't change.

isValid()
true if hex value is in one of the following ranges:
0x61 - 0x7A (a-z)
0x41 - 0x5A (A-Z)
0x20 (space)
"""

def encode(flag):
	var_1 = 32
	for c in flag:
		c = lower(c)
		if c == ' ': c = '{'

		# Main encryption
		# Note: The below values are all numbers, not characters.
		c = ord(c) - ord('a')

		# Loads [0xdc4 (unk_DC4) + c * 8] into eax.
		# Referred to as lookupc.
		# This seems to be a lookup encryption table.
		lookup_table = [0, 8, 20, 34, 44, 48, 60, 72, 82, 88, 104, 116, 128, 138, 146, 160, 174, 190, 200, 208, 214, 224, 236, 248, 6, 22, 36, 114, 39, 119, 97, 0]
		lookupc = lookup_table[c]

		# Loads [0xdc0 (matrix) + c * 8] into edx.
		# Referred to as matrixc.
		# This is another lookup encryption table.
		matrix_table = [8, 12, 14, 10, 4, 12, 12, 10, 6, 16, 12, 12, 10, 8, 14, 14, 16, 10, 8, 6, 10, 12, 12, 14, 16, 14, 4, 69, 32, 110, 73, 100]
		matrixc = lookup_table[c]

		combinedc = lookupc + matrixc

		if lookupc < combinedc:
			char_val = getValue(lookupc)

def getValue(lookupc):
	val = ord(lookupc) + 7
	# CMOVS = Only moves if val > 127.
	if (val > )


