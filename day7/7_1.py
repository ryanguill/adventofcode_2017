import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle

DAY = 7

begin_terminal_block(DAY)
#==============================================================================

towers = []
held_up = set()
bases = set()
for line in read_input(DAY).readlines():
	tower = tuple(line.split())
	if len(tower) > 2:
		base = tower[0]
		bases.add(base)

		for x in tower[3:]:
			held_up.add(x.strip(','))

for base in bases:
	if base not in held_up:
		print(base)



#==============================================================================
end_terminal_block()