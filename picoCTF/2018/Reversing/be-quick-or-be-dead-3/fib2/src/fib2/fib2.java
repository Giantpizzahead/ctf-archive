package fib2;

public class fib2 {
	static int[] fibs;
	static int NUM_FIB = 0x18e28;
	
	public static void main(String[] args) {
		fibs = new int[NUM_FIB + 1];
		for (int i = 0; i < 5; i++) {
			fibs[i] = 0x2345 + (int) Math.pow(i, 2);
		}
		
		int ebx, r12d, mult;
		for (int i = 5; i < NUM_FIB + 1; i++) {
			ebx = fibs[i-1] - fibs[i-2];
			r12d = fibs[i-3] - fibs[i-4];
			ebx += r12d;
			mult = fibs[i-5] * 0x1234;
			fibs[i] = ebx + mult;
		}
		System.out.println(fibs[NUM_FIB]);
	}
	
	// Result: -114593058
	// Flag: picoCTF{dynamic_pr0gramming_ftw_d1b4a912}
}
