import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 13

begin_terminal_block(DAY)
#==============================================================================

levels = {}

for line in read_input(DAY).readlines():
	(level, scanner_range) = [int(x) for x in line.strip().split(': ')]
	levels[level] = scanner_range

delay = 0
while True:
	delay += 1
	caught = False
	for depth in levels:
		if (depth + delay) % ((2 * levels[depth]) - 2) == 0:
			caught = True
			break

	if not caught:
		print('answer', delay)
		break

#==============================================================================
end_terminal_block()
