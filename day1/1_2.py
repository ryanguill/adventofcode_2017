import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...

from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 1

begin_terminal_block(DAY)
#==============================================================================

input = []
for char in read_input(DAY).read():
	input.append(int(char))

toSum = []

for idx, ele in enumerate(input):
	if ele == input[int(idx - len(input) / 2)]:
		toSum.append(ele)

#print(toSum)
print(sum(toSum))		

#==============================================================================
end_terminal_block()

