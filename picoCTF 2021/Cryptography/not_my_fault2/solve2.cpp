#include <iomanip>
#include <iostream>
#include <stdio.h>
#include <vector>
#include <flint.h>
#include <fmpz.h>
#include <fmpz_mod.h>
#include <fmpz_mod_poly.h>
using namespace std;

#define DEBUG true

const char* strN = "146975320698968190565260106200986271117791009112255997487643711870003600883598081268834485671406368075450281421876928838726135489974359610326517044525392544406121326263646260642144986158197747452314042513847441471427278473430133421087724861363391895180988655815339130711119816187042544490030427453604399237087";
const char* stre = "110563215138182921582247642823132153337807436027737934674243095447014135875354168058750848092298825348678116416335449514132138553459693795368409864803141268322041304320938396438515077223451462124135613666158244709032745966050270742099026079913193967975174140288912929767526234658221624847704224697255226248653";
const char* strD = "1024";

flint_rand_t randGen;
fmpz_mod_ctx_t ctxMod;
fmpz_t N, e, x;
int D;

const int MAXD = 262144;
fmpz_mod_poly_t polyParts[MAXD];
fmpz_t yVals[MAXD];

int main(int argc, const char* argv[]) {
	// Setup values & generate random x
	if (argc > 1) {
		strN = argv[1];
		stre = argv[2];
		strD = argv[3];
	}
	fmpz_init(N); fmpz_set_str(N, strN, 10);
	fmpz_init(e); fmpz_set_str(e, stre, 10);
	D = stoi(strD);
	fmpz_sub_ui(N, N, 2);
	flint_randinit(randGen);
	fmpz_init(x); fmpz_randm(x, randGen, N);
	flint_randclear(randGen);
	fmpz_add_ui(x, x, 1);
	fmpz_add_ui(N, N, 2);

	if (DEBUG) {
		printf("N: "); fmpz_print(N); printf("\n");
		printf("e: "); fmpz_print(e); printf("\n");
		printf("D: %d\n", D);
		printf("x: "); fmpz_print(x); printf("\n");
	}

	// Generate polynomial pairs
	printf("Generating polynomial parts...\n");
	fmpz_t currX, chgX, tempB;
	fmpz_mod_ctx_init(ctxMod, N);
	fmpz_init_set_ui(currX, 1);
	fmpz_init_set_ui(chgX, 0);
	fmpz_init_set(tempB, N);
	fmpz_sub(tempB, tempB, x);
	fmpz_powm(chgX, x, e, N);
	for (int i = 0; i < D; i++) {
		fmpz_mod_poly_init(polyParts[i], ctxMod);
		fmpz_mod_poly_set_coeff_fmpz(polyParts[i], 0, tempB, ctxMod);
		fmpz_mod_poly_set_coeff_fmpz(polyParts[i], 1, currX, ctxMod);
		fmpz_mod_mul(currX, currX, chgX, ctxMod);
	}

	printf("Polynomials:\n");
	for (int i = 0; i < D; i++) {
		fmpz_mod_poly_print(polyParts[i], ctxMod); printf("\n");
	}

	return 0;
}