import socket, random, time
from randcrack import RandCrack

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("3.22.198.100", 3201))
s.recv(4096)
s.recv(4096)

def gen_iv_and_key():
	s.sendall(bytes("AAAA\n11112222333344445555666677778888\n1\n", "utf-8"))
	result = b""
	while b"for?\n>>> " not in result:
		part = s.recv(4096)
		result += part
	key_loc = result.index(b"The key was ") + 12
	key = int(result[key_loc:key_loc+32], 16)
	iv_loc = result.index(b"you were curious ") + 17
	iv = int(result[iv_loc:iv_loc+32], 16)
	# print(iv)
	# print(key)
	# iv = random.getrandbits(128).to_bytes(16, 'big').hex()
	# key = random.getrandbits(128).to_bytes(16, 'big').hex()
	# iv = int(iv, 16)
	# key = int(key, 16)
	return iv, key

# Submit required numbers to crack random gen
random.seed(time.time())
rc = RandCrack()
for i in range(624//8):
	print("Getting key set", i)
	iv, key = gen_iv_and_key()

	# num = int.from_bytes(iv, byteorder='big')
	num = iv
	num1 = num >> 96
	num2 = (num >> 64) % (1 << 32)
	num3 = (num >> 32) % (1 << 32)
	num4 = (num) % (1 << 32)
	rc.submit(num4)
	rc.submit(num3)
	rc.submit(num2)
	rc.submit(num1)
	# num = int.from_bytes(key, byteorder='big')
	num = key
	num1 = num >> 96
	num2 = (num >> 64) % (1 << 32)
	num3 = (num >> 32) % (1 << 32)
	num4 = (num) % (1 << 32)
	rc.submit(num4)
	rc.submit(num3)
	rc.submit(num2)
	rc.submit(num1)

# Predict next iv and key
'''
actual_iv, actual_key = gen_iv_and_key()
print("Actual IV:", actual_iv)
print("Actual key:", actual_key)
'''
predicted_iv = rc.predict_getrandbits(128)
predicted_key = rc.predict_getrandbits(128)
print("Predicted IV:", predicted_iv)
print("Predicted key:", predicted_key)

s.sendall(bytes("AAAA\n{}\n1\n".format(hex(predicted_key)[2:]), "utf-8"))
while True:
	result = s.recv(4096)
	print(result)
	if len(result) == 0:
		break

# USCC{p53ud0_r4nd0m_d03s_n0t_m34n_tru3_r4nd0m}
