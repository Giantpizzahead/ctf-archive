# https://mathoverflow.net/questions/120160/attack-on-crt-rsa
# picoCTF{1_c4n'7_b3l13v3_17'5_n07_f4ul7_4774ck!!!}

import random
import math
from scipy import fft, ifft
import numpy as np
from Crypto.Util.number import GCD

N = 95268558416113814803320318152166103562983977750076439308089264617322481159448542557329552517803377529941905868376693543257246745315245893686938451228600403391895390293204543002210595204522597500315691778933309000946054331512820598622024659738823821397279147847989553179314383811360125927436848040993488295951
e = 25908226531699495092164549059972112050027524813329260815216706479584045462070445802416124993395751225979858465288108627490603471164841014431369885022481764961538356465679107913980170398016065922927360034295463219729665299644656969088992725657895080845967564904501470814005592753240026184983997465893615798429
D = 1 << 10

x = random.randint(1, N-1)


def poly_mult(A, B):
	L = len(A) + len(B)
	R = [0 for _ in range(L)]
	for i in range(len(A)):
		for j in range(len(B)):
			R[i+j] = (R[i+j] + A[i] * B[j]) % N
	return R


def poly_eval(P, y):
	R = 0
	curr_y = 1
	for i in range(len(P)):
		R = (R + P[i] * curr_y) % N
		curr_y = curr_y * y % N
	return R


# Compute the polynomial
poly = [1, 0]
curr_x = 1
chg_x = pow(x, e, N)
for i in range(D):
	if i % 1000 == 0:
		print('On mult {}'.format(i))
	poly2 = [-x+N, curr_x]
	poly = poly_mult(poly, poly2)
	curr_x = curr_x * chg_x % N

# Evaluate the polynomial
res = []
curr_y = 1
chg_y = pow(x, e*D, N)
for b in range(D):
	if b % 1000 == 0:
		print('On eval {}'.format(b))
	res.append(poly_eval(poly, curr_y))
	curr_y = curr_y * chg_y % N

# Find GCDs
for b in range(D):
	if b % 1000 == 0:
		print('On GCD {}'.format(b))
	gcd = GCD(res[b], N)
	if gcd != 1:
		print('Pos {}, value {} = GCD {}'.format(b, res[b], gcd))
		break

print()
P = gcd
Q = N // gcd
print('P = {}'.format(P))
print('Q = {}'.format(Q))
print('P+Q = {}'.format(P+Q))
