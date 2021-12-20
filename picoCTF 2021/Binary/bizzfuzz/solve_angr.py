import angr
import claripy
import sys
import logging
logging.getLogger('angr').setLevel('INFO')

def main(argv):
	path_to_binary = argv[1]
	project = angr.Project(path_to_binary)

	initial_state = project.factory.entry_state()

	def check_vulnerable(state):
		return state.se.symbolic(state.regs.eip)

	simulation = project.factory.simgr(
		initial_state, 
		save_unconstrained=True,
		stashes={
		'active' : [initial_state],
		'unconstrained' : [],
		'found' : [],
		'not_needed' : []
		}
	)

	def has_found_solution():
		return simulation.found

	def has_unconstrained_to_check():
		return simulation.unconstrained

	def has_active():
		return simulation.active

	while (has_active() or has_unconstrained_to_check()) and (not has_found_solution()):
		for unconstrained_state in simulation.unconstrained:
			def should_move(s):
				return s is unconstrained_state
			simulation.move('unconstrained', 'found', filter_func=should_move)
		simulation.step()

	if simulation.found:
		solution_state = simulation.found[0]
		# Force EIP to a specific pointer
		solution_state.add_constraints(solution_state.regs.eip == 0x4d4c4749)
		for byte in solution_state.posix.files[sys.stdin.fileno()].all_bytes().chop(bits=8):
			solution_state.add_constraints(
				claripy.Or(
				  byte == 0x0,
				  claripy.And(
				    byte >= 'A', 
				    byte <= 'Z'
				  )
				)
			)

		solution = solution_state.posix.dumps(sys.stdin.fileno())
		print(solution)
	else:
		raise Exception('Could not find the solution')
	# explorer = angr.exploration_techniques.explorer.Explorer(avoid=should_avoid)
	# simgr.use_technique(explorer)
	# simgr.stashes['mem_corrupt'] = []
	
	# while len(simgr.active):
	# 	step_simgr(simgr)
	# print('Seen ({}):'.format(len(ordered_addrs)), [hex(x) for x in ordered_addrs][-100:])
	# print('Avoid ({}):'.format(len(simgr.avoid)), [x.posix.dumps(0) for x in simgr.avoid][-100:])
	# print(simgr)
	IPython.embed()

if __name__ == "__main__":
	main(sys.argv)
