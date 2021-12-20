import random
import gmpy2
# import gmpy_cffi as gmpy2
import time
from multiprocessing import Pool

epoch = 1610664666.801864000

right_p = 115077789659953488935864221139659825210347474679662604788595167824377838957202791945244895551365443129092888070502293168577728517096322244732533983982828071422135461093779288147840159774911560707457099573838016281423899399266725005432558229929367023085619299497167136449579175465625295277572802302303510666323
right_q = 87380309481270063392304355840882039413222973548731239730804940740629652843960694290676931317736810886760812548450472978719472163142500492628571589284206229523961960238417688619507334853066454553641515900189626043495351325486918628953613556875205646354581175061721685136267179595462399064349370266844139301117

def test_seed(seed):
	# if abs(round(seed, 4) - seed) < 10**-9: print('On {}'.format(seed))
	random.seed(seed)
	random.getrandbits(1024)
	random.getrandbits(1024)
	p = gmpy2.next_prime(random.getrandbits(1024))
	if p == right_p:
		q = gmpy2.next_prime(random.getrandbits(1024))
		if q == right_q:
			print('FOUND {}\n'.format(epoch) * 20)
			return True
	return False

curr_seed = 1610664666.81
with Pool(5) as p:
	while True:
		start = time.time()
		print('On {}'.format(curr_seed))
		vals = []
		for i in range(10000):
			vals.append(round(curr_seed - i*0.000001, 6))
		# print(vals[:10], vals[-10:])
		if True in p.map(test_seed, vals):
			print('End at {}'.format(curr_seed))
			break
		curr_seed = round(curr_seed - 0.01, 6)
		print('Time: {:.3f} seconds'.format(time.time() - start))
