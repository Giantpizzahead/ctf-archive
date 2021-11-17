import itertools
import hashlib

salt = 'e361bfc569ba48dc'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for p in itertools.product(alphabet, repeat=8):
	plain = salt + ''.join(p)
	h = hashlib.md5(plain.encode()).hexdigest()
	if h.startswith('0e'):
		try:
			int(h[2:])
			print(''.join(p))
			print(h)
			input()
		except Exception as e:
			pass
