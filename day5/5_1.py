import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = 5

begin_terminal_block(DAY)
#==============================================================================

print(read_input(DAY).read())

#==============================================================================
end_terminal_block()
