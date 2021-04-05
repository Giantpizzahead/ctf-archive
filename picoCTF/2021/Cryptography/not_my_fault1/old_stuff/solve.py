'''
Small CRT-Exponent RSA Revisited
Atsushi Takayasu, Yao Lu, and Liqiang Peng
https://www.iacr.org/archive/eurocrypt2017/10210359/10210359.pdf
'''

import sys
import math
import sympy
import fpylll
from fpylll import FPLLL
import copy
import numpy as np
from sympy.abc import x, y, a, b

DEBUG = False


'''
Computes the Euclidean norm of a vector.
'''
def norm_vector(vector):
	return np.linalg.norm(np.array(vector, dtype='float'))


'''
Computes the determinant of an array.
'''
def det_matrix(matrix):
	return abs(np.linalg.det(np.array(matrix, dtype='float')))


'''
Solves R simultaneous integer equations.
Use sympy to pass in the expressions, they will all be set equal to 0!
'''
def solve_equations(equations):
	sol = sympy.solvers.solve(equations)
	print('Solution:', sol)
	print()
	return sol


'''
Applies the LLL algorithm on the given matrix.
'''
def apply_lll(matrix):
	int_matrix = fpylll.IntegerMatrix.from_matrix(matrix)
	int_res = fpylll.LLL.reduction(int_matrix)
	res = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
	_ = int_res.to_matrix(res)
	# res = olll.reduction(matrix, 0.75)
	if DEBUG:
		mat_det = det_matrix(matrix)
		print('New norms:')
		for j in range(len(res)):
			vec_norm = norm_vector(res[j])
			guarantee_norm = (2 ** (len(res)*(len(res)-1)/4/(len(res)-j))) * (mat_det ** (1/(len(res)-j)))
			print('{0:.5} <= {1:.5}'.format(vec_norm, guarantee_norm))
			# assert(vec_norm <= guarantee_norm), 'LLL algorithm check failed!'
		print()
	return res


# Constants
N = 68780746741818052320915303537186121471923617215250694170349110029896582234724030082313794291310576927248835498201988137378996392353086007868035263352486579860353877197885985820527185421970351755612377064739220749592280038795359748069802012765229568654150259372949162555006880222975691058209501319798012035323
e = 63599200122328985120251768461961607399046080388971273760616893981730455164614448652362812684929509856525376711723869411702028042968755499646840424768911336144258273886845428662074691309695249121362444128406896464236740644125806340903753530613080693628080630947442075591935101136075666921713630425186727875241
# For debug only
p = 9745014586169990969
q = 9261408255875296270569722423416106309683362727649445608495063248988454929191533641976070522634514635017335217673631723460986903752453755846201108399471159
d_p = 3899044708779591341
d_q = 489767
MAX_P = math.sqrt(N)
MAX_DQ = 1 << 20

def main():
	# Calculate needed values
	# num_variables = 2
	alpha = math.log(e, N)  # e = N^alpha
	delta = math.log(MAX_DQ, N)  # d_q = N^delta
	beta = math.log(MAX_P, N)  # p = N^beta, q = N^(1-beta)
	# Bounded by values
	X_p = math.ceil(math.pow(N, alpha+beta+delta-1))+10
	X_q = math.ceil(math.pow(N, alpha+beta+delta-1))+10
	Y_p = math.ceil(math.pow(N, beta))+10
	Y_q = math.ceil(math.pow(N, 1-beta))+10

	if DEBUG:
		print('alpha:', alpha)
		print('beta:', beta)
		print('delta:', delta)
		print('X_p, X_q:', X_p)
		print('Y_p:', Y_p)
		print('Y_q:', Y_q)
	# Assuming beta ~ 1/2
	compare_res = (1 - beta - math.sqrt(alpha * beta * (1 - beta)))
	print('compare: {0:.5} < {1:.5}'.format(delta, compare_res))
	assert(delta < compare_res), 'Decrease p, or decrease d_q'
	print()

	# Create matrix
	constants = [1, X_p, X_p*Y_p, Y_p, X_p*Y_p**2, X_q*Y_q]
	variables = [1, x, x*y, y, x*y**2, a*b]
	mat = [
		[e, 0, 0, 0, 0, 0],
		[0, e, 0, 0, 0, 0],
		[N, N, -1, 0, 0, 0],
		[0, 0, 0, e, 0, 0],
		[0, 0, N, N, -1, 0],
		[0, -1, 0, 0, 0, 1]
	]
	for i in range(len(mat)):
		for j in range(len(constants)):
			mat[i][j] *= constants[j]
	mat = apply_lll(mat)
	# print(mat)

	# Remove constants
	for i in range(len(mat)):
		for j in range(len(constants)):
			assert(mat[i][j] % constants[j] == 0)
			mat[i][j] //= constants[j]

	# Generate equations
	equations = []
	for i in range(len(mat)):
		equation = 0
		for j in range(len(variables)):
			equation += mat[i][j] * variables[j]
		equations.append(equation)
		# Try with these equations
		sol = solve_equations(equations)

	if DEBUG:
		print('Equations:')
		print('\n'.join(str(x) for x in equations))
		print()
		# Check if equation solutions match
		corr_x = (e*d_q-1)//(q-1) - 1
		corr_y = p
		print('Correct sol: x = {}, y = {}'.format(corr_x, corr_y))
		for eq in equations:
			dbg_eq = copy.deepcopy(eq)
			dbg_eq = dbg_eq.subs(x, corr_x).subs(y, corr_y)
			# assert(dbg_eq == 0), 'Equation invalid! {} = {}'.format(eq, dbg_eq)


if __name__ == '__main__':
	main()
