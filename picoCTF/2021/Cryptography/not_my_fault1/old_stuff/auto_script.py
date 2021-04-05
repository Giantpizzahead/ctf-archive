import random
from hashlib import md5
from pwn import *

conn = remote('mercury.picoctf.net', 10055)

def main():
	captcha = conn.recvline().decode()
	temp_index = captcha.index('starts with "')
	starts_with = captcha[temp_index+13:temp_index+18]
	temp_index = captcha.index('hex digits: ')
	hex_digits = captcha[temp_index+12:temp_index+18]
	log.info('Starts with ' + starts_with + ', MD5 hash ends with ' + hex_digits)
	alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

	prog = log.progress('Brute-forcing hash...')
	while True:
		test_str = starts_with + ''.join([random.choice(alphabet) for _ in range(10)])
		md5_hash = md5(test_str.encode()).hexdigest()
		if md5_hash.endswith(hex_digits):
			prog.success('Hash found!')
			conn.sendline(test_str)
			break
	
	conn.interactive()


if __name__ == '__main__':
	main()
