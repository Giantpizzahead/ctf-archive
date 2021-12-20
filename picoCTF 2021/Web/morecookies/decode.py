import base64
import requests

def decode_cookie(c):
	c = base64.b64decode(c)
	c = base64.b64decode(c)
	c = [int(i) for i in c]
	return c

def encode_cookie(c):
	c = bytes(c)
	c = base64.b64encode(c)
	c = base64.b64encode(c)
	return c

def change_cookie(c, i, j):
	c[i] = (c[i]+j)%256
	if c[i] < 0: c[i] += 256
	return c

def test_cookie(c):
	r = requests.get('http://mercury.picoctf.net:56136/', cookies=dict(auth_name=c.decode()))
	if 'Cannot decode cookie' in r.text:
		return False
	else:
		return True

COOKIE = 'a1BSYjhHenVHN3Q1ckczWkZpME9IL0oxN2w2clUwcDZZRk4zQ3hkQVI3Zk81ZENZNXduNHk5d3psOFFPQUJZYjRHb2tDVkVHK2FSdmlvVTA3V2hVeGVPMUZ5QzQ1a0IzdWt3MEIybHNZY2QxVE1Kd3dacXoyZkJOVSs1VFg5MXI=='

for i in range(96):
	for j in range(-3, 4, 2):
		print('Testing index {}, change {}'.format(i, j))
		cookie = decode_cookie(COOKIE)
		print(len(cookie))
		blocks = []
		cookie_hex = ''
		for k in cookie:
			if k < 0x10: cookie_hex += '0'
			cookie_hex += hex(k)[2:]
		for k in range(0, len(cookie_hex), 32):
			blocks.append(cookie_hex[k:k+32])
		cookie = change_cookie(cookie, i, j)
		cookie = encode_cookie(cookie)
		if test_cookie(cookie):
			print('\nValid cookie:')
			print('Old:', decode_cookie(COOKIE))
			print('New:', cookie)
			# print('Old:', ' '.join(i[] for i in range(0, len(cookie_hex), 2)))
			# print('\nNew:', ' '.join(hex(i)[2:] for i in cookie))
			print(blocks)
			print('Value:', cookie.decode())
			print(decode_cookie(cookie))

# Changing index 9 appears to produce valid cookies...?
# 