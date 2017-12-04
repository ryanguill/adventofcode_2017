import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 4

begin_terminal_block(DAY)
#==============================================================================
total = 0
for line in read_input(DAY):
	words = line.split()
	distinct_words = set(words)
	if len(words) == len(distinct_words):
		total += 1

print(total)

#==============================================================================
end_terminal_block()
