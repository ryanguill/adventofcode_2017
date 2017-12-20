import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block


DAY = 17

begin_terminal_block(DAY)
#==============================================================================

puzzle_input = 329

current_pos = 0
for idx in range(1, 50000001):
	current_pos = (current_pos + puzzle_input) % idx + 1
	if current_pos == 1:
		answer = idx


print("answer", answer)

#==============================================================================
end_terminal_block()