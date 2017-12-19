import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 15

begin_terminal_block(DAY)
#==============================================================================

#generator a 16807
#generator b 48271

# Generator A starts with 722
# Generator B starts with 354


def gen(factor, prev):
	while True:
		prev = (prev * factor) % 2147483647
		yield prev


count = 0
for i, (a, b) in enumerate(zip(gen(16807, 722), gen(48271, 354))):
	#print(i, bin(a), bin(b))
	if bin(a)[-16:] == bin(b)[-16:]:
		count += 1
	if i > 40000000:
		break


print(count)


#==============================================================================
end_terminal_block()