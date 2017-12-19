import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, neighbors4
from itertools import cycle
from collections import defaultdict
from operator import xor
from functools import reduce

DAY = 14

begin_terminal_block(DAY)
#==============================================================================

def knot_hash(inp):
	def grouped(l, n):
		"""Yield successive n-sized chunks from l."""
		for i in range(0, len(l), n):
			yield l[i:i + n]

	lengths = [ord(x) for x in inp]
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
	return ('').join(hsh)

def make_grid(puzzle_input):
	grid = []

	for line_no in range(128):
		inp = "{}-{}".format(puzzle_input, line_no)
		hsh = knot_hash(inp)

		line = ''
		for char in hsh:
			line += format(int(char, 16), 'b').zfill(4)
		grid.append([int(x) for x in list(line)])
	return grid

grid = make_grid('ljoxqyyw')

count = 0
ones = []
for x in range(128):
	ones += [(x, y) for y, value in enumerate(grid[x]) if value == 1]

while ones:
	queued = [ones[0]]
	while queued:
		(x, y) = queued.pop()
		if (x, y) in ones:
			ones.remove((x, y))
			queued += neighbors4((x, y))
	count += 1

print(count)

#==============================================================================
end_terminal_block()
