import java.util.*;

/**
What the different operators do:
+ = a + b
- = a - b
* = a * b
/ = a // b
^ = a ^ b
| = a | b
& = a & b
% = a % b
f = Returns the 1st number
o = Returns the 2nd number
x = Returns the 2nd number
t = Returns the 1st number
r = Returns the 2nd number

Make sure to handle parentheses. Each number is surrounded by parentheses also.

This is now a programming problem... Good luck me! :)
 */

public class solver {
	String problem;
	boolean DEBUG = false;
	
	solver() {
		System.out.println("Please enter the problem:");
		Scanner s = new Scanner(System.in);
		problem = s.nextLine();
		s.close();
		
		long answer = evaluateExpr();
		System.out.println("The answer is:\n" + answer);
	}
	
	/**
	 * Evaluates the whole expression using a stack.
	 */
	long evaluateExpr() {
		Stack<Token> eval = new Stack<Token>();
		char c;
		Token num1, op, num2;
		for (int i = 0; i < problem.length(); i++) {
			c = problem.charAt(i);
			if (c == ')') {
				// Solve this part of the expression
				num2 = eval.pop();
				op = eval.pop();
				if (op.type == '(') {
					// Only one number; just evaluate that number
					eval.add(new Token(num2.value));
					if (DEBUG) System.out.println("Evaluated number " + eval.peek().value);
				} else {
					num1 = eval.pop();
					eval.pop();  // Pops parentheses
					// Evaluate the operation
					eval.add(new Token(operation(num1.value, num2.value, op.type)));
					if (DEBUG) System.out.println((num1.value) + " " + (op.type) + " " + (num2.value) + " = " + eval.peek().value);
				}
			} else if ('0' <= c && c <= '9') {
				// Parsing a number
				int numStartI = i;
				while ('0' <= c && c <= '9') {
					i++;
					c = problem.charAt(i);
				}
				// Check if this is a negative number
				if (eval.peek().type == '-') {
					// This is a negative number
					eval.pop();
					eval.add(new Token(Long.parseLong(problem.substring(numStartI, i)) * -1));
					if (DEBUG) System.out.println("Negative number " + eval.peek().value);
				} else {
					eval.add(new Token(Long.parseLong(problem.substring(numStartI, i))));
					if (DEBUG) System.out.println("Parsed number " + eval.peek().value);
				}
				i--;
			} else if (c == ' ') {
				// Ignore spaces
				continue;
			} else {
				// Parsing beginning parentheses or operation
				eval.add(new Token(c));
			}
		}
		
		// There should only be one token number at the end
		return eval.pop().value;
	}
	
	/**
	 * Evaluates the given operation based on the rules stated above.
	 */
	long operation(long a, long b, char op) {
		switch (op) {
		case '+': return a + b;
		case '-': return a - b;
		case '*': return a * b;
		case '/': return a / b;
		case '^': return a ^ b;
		case '|': return a | b;
		case '&': return a & b;
		case '%': return a % b;
		case 'f': return a;
		case 't': return a;
		case 'o': return b;
		case 'x': return b;
		case 'r': return b;
		default: return -1;
		}
	}
	
	public static void main(String[] args) {
		new solver();
	}
	
	class Token {
		char type;
		long value;
		
		public Token(char type) {
			this.type = type;
		}
		
		public Token(long value) {
			this.type = 'i';
			this.value = value;
		}
	}
}