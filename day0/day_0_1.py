import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...

from lib.utils import read_input

DAY = 0

print(read_input(DAY).read())

def test_foo():
	assert 1 == 1

def test_bar():
	#assert 1 == 0
	pass
