import itertools
import random
import subprocess
import time
from datetime import datetime
from hashlib import md5
from pwn import *

conn = None

def main(att_num):
	try:
		dt_str = datetime.now().strftime('%H:%M:%S')
		log.info('Starting attempt #{} at {}'.format(att_num, dt_str))
		conn = remote('mercury.picoctf.net', 5833)  #10055)
		captcha = conn.recvline().decode()
		temp_index = captcha.index('starts with "')
		starts_with = captcha[temp_index+13:temp_index+18]
		temp_index = captcha.index('hex digits: ')
		hex_digits = captcha[temp_index+12:temp_index+18]
		log.info('Starts with ' + starts_with + ', MD5 hash ends with ' + hex_digits)
		alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'

		prog = log.progress('Brute-forcing hash')
		hash_found = False
		for alp_str in itertools.product(alphabet, repeat=6):
			test_str = starts_with + ''.join(alp_str)
			md5_hash = md5(test_str.encode()).hexdigest()
			if md5_hash.endswith(hex_digits):
				prog.success('Hash found!')
				conn.sendline(test_str)
				hash_found = True
				break
		if not hash_found:
			prog.failure('Could not decode hash')
			return

		message = conn.recvline().decode()
		temp_index = message.index('Modulus :  ')
		N = int(message[temp_index+11:].strip())
		message = conn.recvline().decode()
		temp_index = message.index('Clue :  ')
		e = int(message[temp_index+8:].strip())
		D = 1 << 16
		log.info('N: ' + str(N))
		log.info('e: ' + str(e))
		log.info('D: ' + str(D))

		# Wait for the prime factors program to either stop or print something
		prog = log.progress('Finding prime factors')
		proc = subprocess.Popen(['./solve', str(N), str(e), str(D)], stdout=subprocess.PIPE)
		stdout_data = ''
		start_time = time.time()
		while proc.poll() is None:
			try:
				stdout_data = proc.communicate(timeout=1)[0].decode()
			except subprocess.TimeoutExpired as e:
				pass
			if len(stdout_data) > 48:
				time.sleep(1)
				proc.terminate()
				break
			elif time.time() - start_time > 840:
				proc.terminate()
				break
			time.sleep(3)
		time.sleep(1)
		stdout_data = proc.communicate()[0].decode()

		# Did the program exit, or print something?
		if len(stdout_data) > 48 and len(stdout_data.strip().split()) >= 3:
			# Printed the answer!
			correct_data = list(map(int, stdout_data.strip().split()))
			prog.success('Found prime factors!')
			log.info('p: ' + str(correct_data[0]))
			log.info('q: ' + str(correct_data[1]))
			log.info('p+q: ' + str(correct_data[2]))
			log.success('*************** GOT THE FLAG ***************')
			conn.sendline(str(correct_data[2]))
			all_data = conn.recvall().strip().decode()
			log.success(all_data)
			with open('auto_flag.txt', 'w') as fout:
				fout.write(all_data)
				fout.write('\n')
			exit(0)
		else:
			# Exited
			prog.failure('Could not find prime factors')

	except Exception as e:
		print(e)


if __name__ == '__main__':
	att_num = 1
	while True:
		try:
			main(att_num)
			att_num += 1
			time.sleep(5)
		except Exception:
			print('Unhandled exception occurred')
			time.sleep(5)
