import angr
import sys
import claripy
import logging
from datetime import datetime
# logging.getLogger('angr').setLevel('INFO')

project = angr.Project('./checkpass', main_opts={'base_addr': 0}, auto_load_libs=False)

s = project.factory.call_state(0x5960, add_options={angr.options.ZERO_FILL_UNCONSTRAINED_MEMORY, angr.options.ZERO_FILL_UNCONSTRAINED_REGISTERS})

print('\nExploring to arg count check')

# Get to arg count check
sm = project.factory.simulation_manager(s)
avoid_addr = [0x593d, 0x62f5, 0x1f1d0, 0x35060, 0x350f0, 0x35220, 0x35350, 0x356a0]
sm.explore(find=0x59ab, avoid=avoid_addr)
s = sm.found[0]

print('\nAt arg count check')
s.block().pp()

# Bypass arg count check
s.mem[0x7fffffffffeff80].int64_t = 2
s = s.step().successors[0]

print('\nAt password length check')
s.block().pp()

# Bypass password length check
s.mem[0x7fffffffffeff70].int64_t = 0x7fffffffffeff00
s.mem[0x7fffffffffeff28].int64_t = 0x29
s = s.step().successors[0]

print('\nAt flag prefix compare')
s.block().pp()

# Add the flag to memory
f_addr = [0x7fffffffffee000, 0x7fffffffffee008, 0x7fffffffffee010, 0x7fffffffffee018, 0x7fffffffffee020, 0x7fffffffffee028]
f_bvs = [s.solver.BVS('f0', 64), s.solver.BVS('f1', 64), s.solver.BVS('f2', 64), s.solver.BVS('f3', 64), s.solver.BVS('f4', 64), s.solver.BVS('f5', 64)]
s.mem[0x7fffffffffeff18].int64_t = 0x7fffffffffee000
for i in range(6):
	# All characters must be printable or null bytes
	for byte in f_bvs[i].chop(8):
		s.add_constraints(byte <= 0x7f)
		# s.add_constraints(byte >= 0x20)
	s.mem[f_addr[i]].int64_t = f_bvs[i]

# Continue
s = s.step().successors[0]
next_2 = s.step().successors
if next_2[0].addr == 0x59f3: s = next_2[0]
else: s = next_2[1]

print('\nAt flag suffix compare')
s.block().pp()

# Continue
s = s.step().successors[0]
next_2 = s.step().successors
if next_2[0].addr == 0x5a0c: s = next_2[0]
else: s = next_2[1]
# Get past dummy compares
s = s.step().successors[0]
s = s.step().successors[0]

print('\nExploring to encryption')

sm = project.factory.simulation_manager(s)
sm.explore(find=0x5b67, avoid=avoid_addr)
s = sm.found[0]
s.solver.simplify()

print('\nExploring encryption round 1/4')
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Takes a bit... (24 sec)
sm = project.factory.simulation_manager(s)
sm.explore(find=0x5b89, avoid=avoid_addr)
s = sm.found[0]
s.solver.simplify()

print('\nExploring encryption round 2/4')
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Takes longer... (160 sec)
sm = project.factory.simulation_manager(s)
sm.explore(find=0x5bb7, avoid=avoid_addr)
s = sm.found[0]
s.solver.simplify()

print('\nExploring encryption round 3/4')
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Takes much longer (1110 sec)
sm = project.factory.simulation_manager(s)
sm.explore(find=0x5be5, avoid=avoid_addr)
s = sm.found[0]
s.solver.simplify()

print('\nExploring encryption round 4/4')
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Doesn't run...?
sm = project.factory.simulation_manager(s)
sm.explore(find=0x5c10, avoid=avoid_addr)
s = sm.found[0]
s.solver.simplify()

print('\nGetting the password...')
print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))

# Get the password?
sm = project.factory.simulation_manager(plz_save)
sm.explore(find=0x62ca, avoid=avoid_addr)
ans = sm.found[0]
ans.solver.simplify()

print('PASSWORD:')
for i in range(6):
	print(ans.solver.eval(f_bvs[i], cast_to=bytes))
