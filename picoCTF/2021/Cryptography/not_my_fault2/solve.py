# https://mathoverflow.net/questions/120160/attack-on-crt-rsa
# Use a divide and conquer approach to make this run fast enough

import datetime
import random
import os
import sys
import math
import sympy
import time
import numpy as np
from scipy import fft, ifft
from sympy.ntheory.modular import crt
from multiprocessing import Pool
from Crypto.Util.number import GCD

DEBUG = True
SMALL_TEST = False

if len(sys.argv) > 1:
	N = int(sys.argv[1])
	e = int(sys.argv[2])
	D = int(sys.argv[3])
else:
	N = 146975320698968190565260106200986271117791009112255997487643711870003600883598081268834485671406368075450281421876928838726135489974359610326517044525392544406121326263646260642144986158197747452314042513847441471427278473430133421087724861363391895180988655815339130711119816187042544490030427453604399237087
	e = 110563215138182921582247642823132153337807436027737934674243095447014135875354168058750848092298825348678116416335449514132138553459693795368409864803141268322041304320938396438515077223451462124135613666158244709032745966050270742099026079913193967975174140288912929767526234658221624847704224697255226248653
	D = 1 << 18
# print('N:', N)
# print('e:', e)
# print('D:', D)

timeout = 840
x = random.randint(1, N-1)

if SMALL_TEST:
	N = 600
	D = 5
	e = 4
	x = 3

def reset_progress(tc):
	global calls, total_calls, next_progress, start_time
	total_calls = tc
	calls = 0
	next_progress = 0
	start_time = time.time()

def log_progress():
	global calls, total_calls, next_progress
	# Update progress
	calls += 1
	if calls*1000 // total_calls > next_progress:
		next_progress = calls*1000 // total_calls
		eta = (time.time()-start_time) / calls * (total_calls-calls)
		print('Progress: {:.1f}% (ETA {})'.format(next_progress/10, datetime.timedelta(seconds=round(eta))))

primes = []
num_primes = math.ceil(math.log(N*N*D, 400000))+1
while len(primes) < num_primes:
	prime = sympy.ntheory.randprime(400000, 405000)
	if prime in primes: continue
	else: primes.append(prime)
primes = sorted(primes)
if SMALL_TEST:
	primes = [7,11,13]
	num_primes = 3
if DEBUG: print('Primes ({}):'.format(len(primes)), primes)


def next_pow2(x):
	return 1<<((x-1).bit_length())


def poly_mult_prime(A, B, P):
	A_f = fft(A)
	B_f = fft(B)
	C = ifft(A_f * B_f).real
	if DEBUG:
		max_error = 0
		for i in range(len(C)):
			max_error = max(abs(C[i]-round(C[i])), max_error)
		if max_error > 0.1:
			print(P, 'size', len(A), '->', max_error)
	for i in range(len(C)): C[i] = round(C[i])
	C = C.astype('int64').tolist()
	for i in range(len(C)): C[i] %= P
	# print(A, '*', B, 'mod', P, '=', C)
	return C


def poly_mult(A, B):
	# Pad
	L = next_pow2(len(A) + len(B))
	while len(A) < L: A.append(0)
	while len(B) < L: B.append(0)
	# FFT for each prime
	list_C = []
	for p in primes:
		a = A[:]
		b = B[:]
		for i in range(L):
			a[i] %= p
			b[i] %= p
		list_C.append(poly_mult_prime(a, b, p))
	# Solve congruences to get actual C
	L = len(list_C[0])
	C = [0 for _ in range(L)]
	for i in range(L):
		cong = []
		for j in range(num_primes):
			cong.append(list_C[j][i])
		val, mod = crt(primes, cong, check=False)
		C[i] = int(val % mod) % N
	# Unpad
	while C[-1] == 0: C.pop()
	# print(A, '*', B, '=', C)
	return C


# Compute the parts of the polynomial (PROVEN TO WORK)
if DEBUG: print('\nComputing polynomial parts')
polys = []
curr_x = 1
chg_x = pow(x, e, N)
for i in range(D):
	polys.append([-x+N, curr_x])
	curr_x = curr_x * chg_x % N

# Divide and conquer to generate the polynomial (PROVEN TO WORK)
def dac(l, r):
	if DEBUG: log_progress()
	if l == r: return polys[l]
	m = (l+r)//2
	return poly_mult(dac(l, m), dac(m+1, r))

if DEBUG:
	reset_progress(2*D-1)
	print('\nGenerating polynomial...')
poly = dac(0, D-1)
if SMALL_TEST:
	print(poly)

# Compute points to evaluate the polynomial at (PROVEN TO WORK)
if DEBUG: print('\nComputing evaluation points')
y_vals = []
curr_y = 1
chg_y = pow(x, e*D, N)
for b in range(D):
	y_vals.append(curr_y)
	curr_y = curr_y * chg_y % N
if SMALL_TEST:
	y_vals = [i for i in range(D)]
	print('y_vals:', y_vals)

# Evaluate polynomial
def eval_rec(P, Y, M):
	if DEBUG: log_progress()
	if len(P) == 1: return {y:P[0] for y in Y}
	# Split into odd and even
	P_even = [0 for _ in range(0, len(P), 2)]
	P_odd = [0 for _ in range(1, len(P), 2)]
	for i in range(0, len(P), 2): P_even[i>>1] = P[i]
	for i in range(1, len(P), 2): P_odd[i>>1] = P[i]
	y2 = set()
	for y in Y: y2.add(y**2 % M)
	x1 = eval_rec(P_even, y2, M)
	x2 = eval_rec(P_odd, y2, M)
	R = {}
	for y in Y:
		ypow = y**2 % M
		R[y] = (x1[ypow] + y*x2[ypow]) % M
	return R

'''
# proven to work
# Correct: {0: 530, 1: 374, 2: 162, 3: 356, 4: 530}

if DEBUG:
	reset_progress(2*D+1)
	print('\nEvaluating polynomial...')
val_dict = eval_rec(poly, set(y_vals), N)
res = []
for i in range(D):
	res.append(val_dict[y_vals[i]])

dict_list = []
small_poly = poly[:]
for i in range(num_primes):
	Y = set()
	for j in y_vals: Y.add(j % primes[i])
	for j in range(len(poly)): small_poly[j] = poly[j] % primes[i]
	dict_list.append(eval_rec(small_poly, Y, primes[i]))
	print(primes[i])
	print(Y)
	print(small_poly)
	print(dict_list[-1])
# print(dict_list)

# Get actual values using CRT
if DEBUG: print('\nGetting evaluation values with CRT...')
res = []
for i in range(D):
	cong = []
	for j in range(num_primes):
		cong.append(dict_list[j][y_vals[i] % primes[j]])
	print(primes, cong)
	val, mod = crt(primes, cong, check=False)
	res.append(int(val % mod) % N)

print(res)
# Check for matching GCD
if DEBUG:
	print('\nChecking for GCD...')
for val in res:
	gcd = GCD(val, N)
	if gcd != 1:
		if DEBUG: os.system('spd-say "A result has been found hello hello yay yay please check quick ok thanks bye bye now"')
		# print('Pos {}, value {} = GCD {}'.format(b, R, gcd))
		# print()
		P = gcd
		Q = N // gcd
		print(P)
		print(Q)
		print(P+Q)
'''

# Evaluate polynomial (Naive)
def eval_num(b):
	print('Eval {}'.format(b))
	curr_y = 1
	y = y_vals[b]
	R = 0
	for coeff in poly:
		R = (R + coeff * curr_y) % N
		curr_y = y * curr_y % N
	gcd = GCD(R, N)
	if gcd != 1:
		if DEBUG: os.system('spd-say "A result has been found hello hello yay yay please check quick ok thanks bye bye now"')
		# print('Pos {}, value {} = GCD {}'.format(b, R, gcd))
		# print()
		P = gcd
		Q = N // gcd
		print(P)
		print(Q)
		print(P+Q)
	return R

mp = Pool()
if DEBUG:
	print('\nEvaluating + Finding GCDs')
	os.system('spd-say "Here we go!"')
nums = [b for b in range(D)]
random.shuffle(nums)
async_res = mp.map_async(eval_num, nums)

# Wait until time limit has passed, then end and give up
start_time = time.time()
while True:
	if async_res.ready() or time.time() - start_time > timeout:
		# Everything is done
		break
	time.sleep(5)
