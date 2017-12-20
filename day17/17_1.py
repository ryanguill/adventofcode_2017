import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block


DAY = 17

begin_terminal_block(DAY)
#==============================================================================

puzzle_input = 329

data = [0]
current_pos = 0
for idx in range(1, 2018):

	current_pos = (current_pos + puzzle_input) % len(data)
	data.insert(current_pos + 1, idx)
	current_pos += 1
	#print(current_pos, data[current_pos], data)

print(data[current_pos+1])

#==============================================================================
end_terminal_block()