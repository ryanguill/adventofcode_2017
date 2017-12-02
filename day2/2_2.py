import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block
from itertools import combinations

DAY = 2

begin_terminal_block(DAY)
#==============================================================================

total = 0
for line in read_input(DAY):
	line = line.split()
	line = list(map(int, line))

	for i in combinations(line, 2):
		if max(i) % min(i) == 0:
			total += max(i) // min(i)
			break

print(total)

#==============================================================================
end_terminal_block()
