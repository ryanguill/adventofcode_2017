import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...

from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 1

begin_terminal_block(DAY)

toSum = []
lastChar = None
firstChar = None
for char in read_input(DAY).read():
	#print(char)
	if firstChar is None:
		firstChar = char
	if char == lastChar:
		toSum.append(int(char))
	lastChar = char

if char == firstChar:
	toSum.append(int(char))

print(toSum)
print(sum(toSum))		

# too low 993

end_terminal_block()

