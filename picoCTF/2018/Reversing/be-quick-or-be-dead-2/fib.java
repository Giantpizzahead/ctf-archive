package fib;

public class fib {
	static int[] fibs;
	static int NUM_FIB = 1067;
	
	public static void main(String[] args) {
		fibs = new int[NUM_FIB + 1];
		fibs[1] = 1;
		fibs[2] = 1;
		for (int i = 3; i < NUM_FIB + 1; i++) {
			fibs[i] = fibs[i-1] + fibs[i-2];
		}
		System.out.println(fibs[NUM_FIB]);
		
		// Results = 781077913
		// Replace the key with that in the program
		// Flag: picoCTF{the_fibonacci_sequence_can_be_done_fast_ec58967b}
	}
}
