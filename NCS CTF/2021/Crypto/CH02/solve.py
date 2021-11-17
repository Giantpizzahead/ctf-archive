import enchant

msg = ['2e310d15730618003c27392502592f1b016e1b1c364505191302', '27271e1d6f3935381618340a740404152d0063160106490a0a050d013d2e', '313c0d45350d0c026f3d236b361120191e373c1c3a080e0c2b04', '1b060c2749020b354105271616532f27772f1c204811111745320b10021717']
english_dict = enchant.Dict('en_US')

def try_pair(a, b):
	l = min(len(a), len(b))
	c = []
	for i in range(0, l, 2):
		x = int(a[i:i+2], 16)
		y = int(b[i:i+2], 16)
		z = x ^ y
		h = hex(z)[2:]
		if len(h) == 1: h = '0' + h
		print(h, end=' ')
		c.append(z)
	print()
	print('Message 1 [{}]:'.format(len(c)))
	# Try to guess the plaintexts
	alp = 'abcdefghijklmnopqrstuvwxyz .:!?;-,0123456789'
	for z in c:
		for x in alp:
			y = chr(ord(x) ^ z)
			if ord(y) < ord(x): continue
			if y not in alp: continue
			print('{}-{}'.format(x, y), end=' ')
		print()
	testa = ['h', 'aieu', 'acdfeghjiklnmoprqstvuwxz', 'ezmrfygxhwivjuktlsnqop']
	testb = [' ', 'nfjz', 'cafdgejhkinlomrpsqvtwuzx', 'zermyfxgwhviujtkslqnpo']
	for a in range(len(testa[0])):
		for b in range(len(testa[1])):
			for c in range(len(testa[2])):
				for d in range(len(testa[3])):
					w1 = 'S' + testa[0][a] + testa[1][b] + testa[2][c] + testa[3][d] + 'y'
					w2 = testb[0][a] + testb[1][b] + testb[2][c] + testb[3][d]
					if not english_dict.check(w1) or not english_dict.check(w2): continue
					print('{} / {}'.format(w1, w2))
	print()

for i in range(4):
	for j in range(4):
		if i == j: continue
		if i != 0 or j != 2: continue
		print('Pair {} and {}'.format(i, j))
		try_pair(msg[i], msg[j])

'''
Pair 0 and 2
1f 0d 00 50 46 0b 14 02 53 1a 1a 4e 34 48 0f 02 1f 59 27 00 0c 4d 0b 15 38 06 
Message 1 [26]:
t-k
h-e
e-e
 -p
f- 
l-g
a-u
g-e
 -s
i-s
s-i
 -n
S-g
h-  :-r !-i
i-f n-a e-j u-z
m-o p-r c-a n-l d-f e-g h-j i-k q-s t-v u-w x-z 
m-r e-z f-y g-x h-w i-v j-u k-t l-s n-q o-p  -? 
y-  .-w :-c !-x ?-f 
S-t A-f B-e C-d D-c E-b F-a H-o I-n J-m K-l L-k M-j N-i O-h P-w Q-v R-u T-s V-q U-r W-p
h-h a-a b-b c-c d-d e-e f-f g-g i-i j-j k-k l-l m-m n-n o-o p-p q-q r-r s-s t-t u-u v-v w-w x-x y-y z-z  -  .-. :-: !-! ?-? 
i-e a-m b-n c-o d-h f-j g-k t-x u-y v-z 
m-  .-c :-w !-l ?-r 
m-f a-j b-i c-h d-o e-n g-l q-z r-y s-x 
y-l a-t b-w c-v d-q e-p f-s g-r m-x o-z 
Y-a
a-g b-d c-e h-n i-o j-l k-m p-v q-w r-t s-u 

the flag is ShimmyShimmyYa
keep guessing
'''