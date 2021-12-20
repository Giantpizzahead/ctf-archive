'''
Password:
D1v1d3AndC0nqu3r

Flag:
picoCTF{r011ing_y0ur_0wn_crypt0_15_h4rd!_06746440}

Part 1: Given

Part 2:
('d3An', [191, 241, 38, 220]) - DEF THIS
('ZhtY', [191, 241, 38, 156])

Part 3:
('dC0n', [179, 7, 0, 0]) - DEF THIS
('tWpX', [167, 179, 7, 0])
('K0CN', [186, 179, 7, 0])

Part 4 (started with this because of call rsi; ret)
('qu3r', [0, 255, 214, 195]) - VERY LIKELY DIVIDEANDCONQUER
('sy0F', [255, 214, 195, 66])
('AWI0', [255, 214, 195, 173])
('YP99', [76, 255, 214, 195])
('842t', [255, 214, 195, 65])

Code might look like:
mov rsi, rdi
movabs rdi, 0x7B3DC26F1
call rsi
ret

0:  48 89 fe                mov    rsi,rdi
3:  48 bf f1 26 dc b3 07    movabs rdi,0x7b3dc26f1
a:  00 00 00
d:  ff d6                   call   rsi
f:  c3                      ret
'''

import hashlib
import itertools

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# alphabet = ' !-.?_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# print('Alphabet length: {}'.format(len(alphabet)))

salt = 'RGiledp6'
substr_l = 7
res = [0 for _ in range(4)]
viable = []

num_iters = 0
total_iters = len(alphabet)**4
for chars in itertools.product(alphabet, repeat=4):
	num_iters += 1
	if num_iters % 1000000 == 0:
		print('Progress: {:.2f}%'.format(num_iters / total_iters * 100))

	# Generate hash
	tohash = ''.join(chars) + salt
	res_str = hashlib.md5(tohash.encode()).hexdigest()
	for i in range(4):
		res[i] = int(res_str[(substr_l+i)*2:(substr_l+i+1)*2], 16)
	# Look for a pattern (call rsi)
	for j in range(2):
		if res[j] == 0xb3 and res[j+1] == 0x07 and res[j+2] == 0x00:
			viable.append((''.join(chars), res[:]))
			break
	# print(tohash, [hex(r) for r in res])

for x in viable:
	print(x)
print('Num viable: {}'.format(len(viable)))
