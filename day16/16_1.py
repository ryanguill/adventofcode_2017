import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block


DAY = 16

begin_terminal_block(DAY)
#==============================================================================


state = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
for inst in read_input(DAY).readline().split(','):
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
		quit

print(('').join(state))

#==============================================================================
end_terminal_block()