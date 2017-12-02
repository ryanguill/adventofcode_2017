import re
import math
from hashlib import sha1, sha256, sha512
import requests

def read_input(day):
	"Open this day's input file"
	filename = './day{}/input.txt'.format(day)
	try:
		return open(filename)
	except FileNotFoundError:
		print("[Notice] Could not find input file: " + filename)
		r = requests.get('http://adventofcode.com/2017/day/{}/input'.format(day), cookies=dict(session='53616c7465645f5f8aedf70c9e9f98b5e6518f0fd988d38f7896315c65900434cf316adfce597de58d6da56fb1da3dc7'))
		with open(filename, 'wb') as fd:
			for chunk in r.iter_content(chunk_size=128):
				fd.write(chunk)
		print("[Notice] input file downloaded.\n\n")
		return read_input(day)

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

def begin_terminal_block(day):
	print('--------------------------------------------------------------------------------')
	print('-----------------------------------Day {}----------------------------------------'.format(day))
	print('--------------------------------------------------------------------------------')
	print('\n\n')

def end_terminal_block():
	print('\n\n')
	print('--------------------------------------------------------------------------------')
	print('--------------------------------------------------------------------------------')
	print('--------------------------------------------------------------------------------')

def memoize(f):
	memo = {}
	def helper(x):
		if x not in memo:
			memo[x] = f(x)
		return memo[x]
	return helper

def hash_sha1(input):
	hash = sha1()
	hash.update(input.encode())
	return hash.hexdigest()

def test_hash_sha1():
	assert hash_sha1('foo') == '0beec7b5ea3f0fdbc95d0dd47f3c5bc275da8a33'

def hash_sha256(input):
	hash = sha256()
	hash.update(input.encode())
	return hash.hexdigest()

def test_hash_sha256():
	assert hash_sha256('foo') == '2c26b46b68ffc68ff99b453c1d30413413422d706483bfa0f98a5e886266e7ae'

def hash_sha512(input):
	hash = sha512()
	hash.update(input.encode())
	return hash.hexdigest()

def test_hash_sha512():
	assert hash_sha512('foo') == 'f7fbba6e0636f890e56fbbf3283e524c6fa3204ae298382d624741d0dc6638326e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'