import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block


DAY = 16

begin_terminal_block(DAY)
#==============================================================================

state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']

instructions = read_input(DAY).readline().split(',')

def perform_instruction (state, inst):
	if inst[0] == 's':
		x = int(inst[1:])
		state = state[(x * -1):] + state[:len(state)-x]
	elif inst[0] == 'x':
		x = inst[1:]
		a, b = x.split('/')
		state[int(a)], state[int(b)] = state[int(b)], state[int(a)]
	elif inst[0] == 'p':
		x = inst[1:]
		a, b = x.split('/')
		idxA = state.index(a)
		idxB = state.index(b)
		state[idxA], state[idxB] = state[idxB], state[idxA]
	else:
		print('something went wrong', inst)
		quit()
	return state

def run (iterations, state, instructions):
	seen = []
	for idx in range(iterations):
		state_joined = ''.join(state)
		if state_joined in seen:
			return seen[iterations % idx]
		seen.append(state_joined)

		for inst in instructions:
			state = perform_instruction(state, inst)

print(run(1000000000, state, instructions))


#==============================================================================
end_terminal_block()

