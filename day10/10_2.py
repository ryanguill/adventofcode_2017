import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import begin_terminal_block, end_terminal_block
from itertools import cycle
from operator import xor
from functools import reduce

DAY = 10

begin_terminal_block(DAY)
#==============================================================================

#Lengths larger than the size of the list are invalid

def grouped(l, n):
	"""Yield successive n-sized chunks from l."""
	for i in range(0, len(l), n):
		yield l[i:i + n]

puzzle_input = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'

lengths = [ord(x) for x in puzzle_input]
lengths += [17, 31, 73, 47, 23]

data = list(range(256))

rounds = 64
current_index = 0
current_skip = 0

for _ in range(rounds):
	for length in lengths:

		data = data[current_index:] + data[:current_index]
		data = list(reversed(data[:length])) + data[length:]
		offset = (len(data) - current_index) % len(data)
		data = data[offset:] + data[:offset]
		current_index = (current_index + length + current_skip) % len(data)
		current_skip += 1



dense = [reduce(xor, chunk) for chunk in grouped(data, 16)]

hsh = ["{0:0{1}x}".format(dec, 2) for dec in dense]


answer = ('').join(hsh)
print(answer, len(answer))


#==============================================================================
end_terminal_block()
