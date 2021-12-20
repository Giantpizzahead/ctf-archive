import gmpy2
import math
import itertools

with open('raw2.txt', 'r') as fin:
	raw = fin.readlines()

last_00 = False

def parse_raw(i):
	global last_00
	# print(i, end=' ')
	if raw[i][0] == 'C':
		# Client
		packet = bytes.fromhex(raw[i][2:])
		if packet[0] == 0:
			# Requesting new public key from the server
			# print('Public key request')
			last_00 = True
			return ('request')
		else:
			# Encrypted message
			# print('Sent encrypted message') # {}'.format(packet[2:]))
			return ('sent', int.from_bytes(packet[1:], byteorder="big"))
	else:
		# Server
		packet = bytes.fromhex(raw[i])
		if packet[0] == 0:
			# Getting a new key
			e = int.from_bytes(packet[1:4], byteorder="big")
			if last_00:
				# Public key
				n = int.from_bytes(packet[4:260], byteorder="big")
				print('public')
				# print('New public key e={} n={}'.format(e, n))
				last_00 = False
				return ('public', e, n)
			else:
				# Private key
				p = int.from_bytes(packet[4:132], byteorder="big")
				q = int.from_bytes(packet[132:260], byteorder="big")
				print('private {} {}'.format(p, q))
				# print('New private key e={} p={} q={}'.format(e, p, q))
				return ('private', e, p, q)
		else:
			# Receiving encrypted message
			# print('Received encrypted message')
			return ('received', int.from_bytes(packet[1:], byteorder="big"))

def encrypt(p, e, n):
	guess = int.from_bytes(p.encode("utf-8"), byteorder="big")
	enc = pow(guess, e, n)
	return enc

keys = []
special = None

seen_private = set()
seen_public = set()

prime_pairs = []

for i in range(len(raw)):
	res = parse_raw(i)
	'''
	if i == 72:
		priv = gmpy2.invert(res[1], (res[2]-1) * (res[3]-1))
		special = (int(priv), res[2] * res[3])
	'''
	if res[0] == 'private':
		# Track private keys
		priv = gmpy2.invert(res[1], (res[2]-1) * (res[3]-1))
		key = (int(priv), res[2] * res[3])
		keys += [key]
		if key in seen_private:
			print('SEEN', key)
		seen_private.add(key)
		prime_pairs += [(res[2], res[3])]
	elif res[0] == 'received':
		# Decrypt the message
		'''
		if i == 140:
			msg = pow(res[1], special[0], special[1])
			msg = pow(res[1], keys[0][0], keys[0][1])
		else:
		'''
		msg = pow(res[1], keys[0][0], keys[0][1])
		keys = keys[1:]
		# print(msg.to_bytes(256, byteorder="big").lstrip(b'\x00'))
	elif res[0] == 'public':
		# Track public keys
		key = (res[1], res[2])
		keys += [key]
		if key in seen_public:
			print('SEEN', key)
		seen_public.add(key)
	elif res[0] == 'sent':
		# Try to decrypt the message
		e, n = keys[0]
		keys = keys[1:]
		'''
		guesses = [
			'Do you want to play a game?',
			'Wanna play a game?',
			'Want to play a game?',
			'Let\'s play a game.',
			'Let\'s play a game!',
			'Ok.',
			'Ok!',
			'Sure.',
			'No.',
			'No',
			'Yes',
			'Yes.',
			'No problem!',
			'No problem',
			'No problem.',
			'Nice.',
			'Nice!',
			'Nice',
			'Not bad.',
			'Not bad!',
			'Not bid',
			'Good job.',
			'Good job!',
			'Good job',
			'Nice work.',
			'Nice work!',
			'Nice work',
			'Fine',
			'Fine.',
			'Fine!',
		]
		for guess in itertools.permutations('abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.?!', r=2): #guesses:
			guess = ''.join(guess)
			enc = encrypt(guess, e, n)
			if enc == res[1]:
				print('CORRECT', res[1], enc)
		'''
		

for a in prime_pairs:
	for b in seen_public:
		if a[0] * a[1] == b[1]:
			print('REUSED', a[0], a[1], b[1])
		if math.gcd(a[0], b[1]) != 1 or math.gcd(a[1], b[1]) != 1:
			print('GCD prime', a[0], a[1], b[1])

for a in seen_public:
	for b in seen_public:
		if a[1] != b[1] and math.gcd(a[1], b[1]) != 1:
			print('GCD public', a[1], b[1])
