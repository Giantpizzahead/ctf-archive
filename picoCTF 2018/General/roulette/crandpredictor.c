#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main () {
   int i, n;
   time_t t;
   
   n = 20;
   
   /*
    *    Intializes random number generator
    *    Replace this with the seed that the roulette
    *    program gives you
    */
   srand(2145);

   /*
    *    Print the next 20 roulette numbers
    *    These will only be accurate if you win every time!
    */
   for( i = 0 ; i < n ; i++ ) {
      printf("%d\n", (rand() + 1) % 36);
      rand();
   }
   
   return(0);
}
