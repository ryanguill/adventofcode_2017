import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle
from collections import defaultdict
from operator import xor
from functools import reduce

DAY = 14

begin_terminal_block(DAY)
#==============================================================================

def knot_hash (inp):
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


puzzle_input = 'ljoxqyyw'

grid = []

used_count = 0;

for line_no in range(128):
	inp = "{}-{}".format(puzzle_input, line_no)
	hsh = knot_hash(inp)

	line = ''
	for char in hsh:
		line += format(int(char, 16), 'b').zfill(4)

	used_count += line.count('1')

	grid.append(line)

print(used_count)


#==============================================================================
end_terminal_block()