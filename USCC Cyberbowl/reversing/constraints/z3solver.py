from z3 import *

flag = []
for i in range(53):
    flag.append(BitVec(str(i), 8))

s = Solver()
for i in range(53):
    s.add(flag[i] >= 32, flag[i] <= 127)

constraints = []
with open('reversing/constraints/constraints4.txt', 'r') as fin:
    constraints = fin.readline().split(', ')
    constraints = [eval(x) for x in constraints]
    # print(constraints)
s.add(*constraints)
s.check()
m = s.model()

solution = [0 for _ in range(53)]
for d in m.decls():
    solution[int(d.name())] = m[d]

print(' '.join([str(x) for x in solution]))
print(''.join([chr(int(str(x))) for x in solution]))

# USCC{I_reaaaaaaaaally_hope_you_used_a_tool_for_th1s}