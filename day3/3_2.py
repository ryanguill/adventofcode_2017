import math
import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, neighbors8

DAY = 3

begin_terminal_block(DAY)
#==============================================================================

puzzle_input = 347991

def calculate_point(grid, x, y):
	neighbors = neighbors8((x, y))
	total = 0
	for (a, b) in neighbors:
		total += grid[a][b]

	return total


def main(inp):
	grid = [[0 for x in range(-250, 250)] for y in range(-250, 250)]
	x = y = 0
	grid[x][y] = 1
	k = 1
	while True:
		for _ in range(k):
			x += 1
			a = calculate_point(grid, x, y)
			if a > inp:
				return a
			grid[x][y] = a

		for _ in range(k):
			y += 1
			a = calculate_point(grid, x, y)
			if a > inp:
				return a
			grid[x][y] = a

		k += 1

		for _ in range(k):
			x -= 1
			a = calculate_point(grid, x, y)
			if a > inp:
				return a
			grid[x][y] = a


		for _ in range(k):
			y -= 1
			a = calculate_point(grid, x, y)
			if a > inp:
				return a
			grid[x][y] = a

		k += 1

print(main(puzzle_input))

#==============================================================================
end_terminal_block()
