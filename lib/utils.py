import re
import math

def read_input(day):
	"Open this day's input file"
	filename = './day{}/input.txt'.format(day)
	try:
		return open(filename)
	except FileNotFoundError:
		print("Cannot find " + filename)

def test_input():
	assert read_input(0).read() == 'day0 test input'

def grep(pattern, lines):
	"Return lines that match pattern"
	output = []
	for line in lines:
		if re.search(pattern, line):
			output.append(line)
	return output

def test_grep():
	data = ['one', 'two', 'three', 'four', 'five']
	assert grep('x', data) == []
	assert grep('o', data) == ['one', 'two', 'four']
	assert grep('ive', data) == ['five']

def X(point):
	return point[0]

def Y(point):
	return point[1]

def test_x_y():
	assert X((1, 1)) == 1
	assert X((2, 0)) == 2
	assert Y((1, 3)) == 3
	assert Y((0, 0)) == 0

def neighbors4(point):
	"The four neighbors, N/E/S/W"
	x, y = point
	return ((x, y+1), (x+1, y), (x, y-1), (x-1, y))

def test_neighbors4():
	assert neighbors4((1, 1)) == ((1, 2), (2, 1), (1, 0), (0, 1))

def neighbors8(point):
	"the eight neighbors, N/NE/E/SE/S/SW/W/NW"
	x, y = point
	return ((x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1))

def test_neighbors8():
	assert neighbors8((0, 0)) == ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

def manhattan_distance(p, q=(0, 0)):
	"returns manhattan (city block) distance between two points"
	return abs(X(p) - X(q)) + abs(Y(p) - Y(q))

def test_manhattan_distance():
	assert manhattan_distance((1, 1)) == 2
	assert manhattan_distance((10, 9), (9, 8)) == 2
	assert manhattan_distance((2, 5), (4, 8)) == 5

def euclidean_distance(p, q=(0, 0)):
	return math.hypot(X(p) - X(q), Y(p) - Y(q))

def test_euclidean_distance():
	assert euclidean_distance((3, 4)) == 5

	

