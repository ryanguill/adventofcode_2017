import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import begin_terminal_block, end_terminal_block
from itertools import cycle

DAY = 10

begin_terminal_block(DAY)
#==============================================================================

#Lengths larger than the size of the list are invalid

lengths = [int(x) for x in '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'.split(',')]
#print(lengths)

data = list(range(256))

current_index = 0
current_skip = 0

"""
Plan:
to handle the reversing of the list,
find the offset from the beginning of the list to the first of the range that needs
to be reversed
slice that off and put it on the end
do the reverse
slice that same number off the end and put it back on the front
"""

#testing
#lengths = [3, 4, 1, 5]
#data = [0, 1, 2, 3, 4]

for length in lengths:

	#print('length:', length)
	#print('start', data, 'current_index', current_index, 'current_skip', current_skip)
	#take the front and put it on the back
	data = data[current_index:] + data[:current_index]
	#print('shifted', data)
	#print('reversed', list(reversed(data[:length]))

	data = list(reversed(data[:length])) + data[length:]
	#print('after reversed', data)
	#take the back and put it back on the front
	offset = (len(data) - current_index) % len(data)
	data = data[offset:] + data[:offset]
	#print('un-shifted', data)

	current_index = (current_index + length + current_skip) % len(data)
	current_skip += 1

print(data)
print(data[0] * data[1])

#==============================================================================
end_terminal_block()