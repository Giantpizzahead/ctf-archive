#pragma GCC optimize("Ofast")
#include <chrono>
#include <cmath>
#include <ctime>
#include <execution>
#include <iomanip>
#include <iostream>
#include <mutex>
#include <stdarg.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <gmp.h>
#include <gmpxx.h>
using namespace std;

using bigint = mpz_class;
using bigintr = mpz_t;
#define raw get_mpz_t()
#define DEBUG false
#define debug if (DEBUG) cout

const char* strN = "146975320698968190565260106200986271117791009112255997487643711870003600883598081268834485671406368075450281421876928838726135489974359610326517044525392544406121326263646260642144986158197747452314042513847441471427278473430133421087724861363391895180988655815339130711119816187042544490030427453604399237087";
const char* stre = "110563215138182921582247642823132153337807436027737934674243095447014135875354168058750848092298825348678116416335449514132138553459693795368409864803141268322041304320938396438515077223451462124135613666158244709032745966050270742099026079913193967975174140288912929767526234658221624847704224697255226248653";
const char* strD = "1024";

bigint N, e, D, x;
const int MAXD = 1 << 16;
int nums[MAXD];
bigintr polyA[MAXD], polyB[MAXD], yVals[MAXD];

int main(int argc, const char* argv[]) {
	if (argc > 1) {
		strN = argv[1];
		stre = argv[2];
		strD = argv[3];
	}
	N = strN;
	e = stre;
	D = strD;
	x = 0;
	gmp_randstate_t randstate;
	gmp_randinit_default(randstate);
	gmp_randseed_ui(randstate, time(NULL));
	N -= 2;
	mpz_urandomm(x.raw, randstate, N.raw);
	N += 2;
	x += 1;

	debug << "N: " << N << endl;
	debug << "e: " << e << endl;
	debug << "D: " << D << endl;
	debug << "x: " << x << endl;
	cout << fixed << setprecision(2);

	// Generate polynomial parts
	debug << "\nGenerating polynomial parts..." << endl;
	bigint currX = 1;
	bigint chgX = 0;
	mpz_powm(chgX.raw, x.raw, e.raw, N.raw);
	for (int i = 0; i < D; i++) {
		bigint B = N-x;
		mpz_init_set(polyA[i], B.raw);
		mpz_init_set(polyB[i], currX.raw);
		currX = currX * chgX % N;
	}

	// Generate evaluation points
	debug << "\nGenerating evaluation points..." << endl;
	bigint currY = 1;
	bigint chgY = 0;
	bigint eD = e*D;
	mpz_powm(chgY.raw, x.raw, eD.raw, N.raw);
	for (int i = 0; i < D; i++) {
		mpz_init_set(yVals[i], currY.raw);
		currY = currY * chgY % N;
	}

	// for (int i = 0; i < D; i++) cout << polyA[i] << ' ' << polyB[i] << endl;
	// for (int i = 0; i < D; i++) cout << yVals[i] << ' ';
	// cout << endl;

	// Evaluate polynomial at the evaluation points
	debug << "\nEvaluating polynomial...\n" << endl;
	bigintr rawN;
	mpz_init_set(rawN, N.raw);
	chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
	int intD, numDone = 0;
	mpz_export(&intD, NULL, 1, sizeof(int), 0, 0, D.raw);
	int updFreq = 100;
	bool primesFound = false;
	mutex m;

	for_each(
		execution::par_unseq,
		yVals,
		yVals+intD,
		[&](bigintr& y) {
			if (primesFound) return;
			if (DEBUG) {
				lock_guard<mutex> guard(m);
				if (numDone % updFreq == 0 && numDone) {
					chrono::steady_clock::time_point curr = std::chrono::steady_clock::now();
					double timeSec = chrono::duration_cast<chrono::microseconds>(curr-begin).count() / 1000000.0;
					double workLeft = (double)(intD-numDone)/numDone;
					double timeToGo = timeSec * workLeft;
					cout << "On " << numDone << " (ETA " << timeToGo << "s)" << endl;
				}
				numDone++;
			}
			bigintr R, part, gcd;
			mpz_inits(part, gcd, NULL);
			mpz_init_set_ui(R, 1);
			for (int j = 0; j < intD; j++) {
				// Best time: 4096, 2.58s
				mpz_set(part, polyA[j]);
				mpz_addmul(part, polyB[j], y);
				mpz_mod(part, part, rawN);
				mpz_mul(R, R, part);
				mpz_mod(R, R, rawN);
			}
			mpz_gcd(gcd, R, rawN);
			if (mpz_cmp_ui(gcd, 1) > 0) {
				// Found primes!
				lock_guard<mutex> guard(m);
				primesFound = true;
				bigint P = N / bigint(gcd);
				bigint Q = N / P;
				debug << "Y value #" << &y-yVals << endl;
				cout << P << "\n";
				cout << Q << "\n";
				cout << P+Q << endl;
			}
		}
		);

	chrono::steady_clock::time_point curr = std::chrono::steady_clock::now();
	double timeSec = chrono::duration_cast<chrono::microseconds>(curr-begin).count() / 1000000.0;
	debug << "DONE [Time taken: " << timeSec << "s]" << endl;
	return 0;
}