import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 5

begin_terminal_block(DAY)
#==============================================================================

instructions = []
for line in read_input(DAY).readlines():
	instructions.append(int(line.strip()))

current_pos = 0
current_iteration = 0

while True:
	current_iteration += 1
	next_pos = current_pos + instructions[current_pos]
	instructions[current_pos] += 1
	current_pos = next_pos

	if current_pos > len(instructions) -1 or current_pos < 0:
		break

print(current_iteration)


#==============================================================================
end_terminal_block()
