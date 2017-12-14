import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle
from collections import defaultdict

DAY = 13

begin_terminal_block(DAY)
#==============================================================================

def scanner_pos (scanner_range, second):
	data = list(range(scanner_range)) + list(reversed(range(scanner_range - 1)))[:-1]
	return data[second % len(data)]

levels = defaultdict(int)

for line in read_input(DAY).readlines():
	(level, scanner_range) = [int(x) for x in line.strip().split(': ')]
	levels[level] = scanner_range


severity = 0

for tick in range(max(levels)):
	scanner_range = levels[tick]
	if scanner_range != 0 and scanner_pos(scanner_range, tick) == 0:
		severity += tick * scanner_range

print(severity)

#==============================================================================
end_terminal_block()