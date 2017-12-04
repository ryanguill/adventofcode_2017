import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 4

begin_terminal_block(DAY)
#==============================================================================

total = 0
for line in read_input(DAY):
	words = [('').join(word) for word in list(map(sorted, line.split()))]
	distinct_words = set(words)
	if len(words) == len(distinct_words):
		total += 1

print(total)

#==============================================================================
end_terminal_block()
