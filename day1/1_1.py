import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...

from lib.utils import read_input, begin_terminal_block, end_terminal_block, memoize

DAY = 1


def test(a):
	return a * 2;



begin_terminal_block(DAY)

for line in read_input(DAY):
	line = line.strip('\n')
	print(line)

end_terminal_block()	
