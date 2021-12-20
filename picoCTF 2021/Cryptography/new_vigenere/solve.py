import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

# First part must be 3, 6, or 7
enc_str = "ilnipdjheipnenhhedionepegiejmleoehejfcnimdgehimnepedhhfbafmcgdek"
enc = []
for c in enc_str:
	enc.append(ord(c) - LOWERCASE_OFFSET)
dec = [0 for _ in range(len(enc))]

key_length = 9
key = [2, 9, 10, 1, 9, 1, 3, 1, 1]
for k in range(key_length):
	vals = []
	for i in range(k, len(enc), key_length):
		c = (enc[i] - key[k] + len(ALPHABET)) % len(ALPHABET)
		vals.append(c)
		dec[i] = c
	print(vals)

for i in range(0, len(dec), 2):
	print(hex(dec[i])[2:], end='')
	print(hex(dec[i+1])[2:], end=' ')
print()

for i in range(0, len(dec), 2):
	c = chr(dec[i]*16+dec[i+1])
	print(c, end='')
print()
