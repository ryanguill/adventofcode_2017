import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 2

begin_terminal_block(DAY)
#==============================================================================

total = 0
for line in read_input(DAY):
	line = line.strip('\n').split('\t')
	line = list(map(int, line))
	total += int(max(line))-int(min(line))

print(total)

#==============================================================================
end_terminal_block()
