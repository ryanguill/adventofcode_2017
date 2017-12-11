import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle

DAY = 11

begin_terminal_block(DAY)
#==============================================================================



def cube_distance(a, b):
	return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) / 2

def move (pos, direction):
	x, y, z = pos
	if direction == 'n':
		return (x, y + 1, z -1)
	elif direction == 'ne':
		return (x + 1, y, z - 1)
	elif direction == 'se':
		return (x + 1, y - 1, z)
	elif direction == 's':
		return (x, y - 1, z + 1)
	elif direction == 'sw':
		return (x - 1, y, z + 1)
	elif direction == 'nw':
		return (x - 1, y + 1, z)
	else:
		print('unknown direction', direction)
		quit()


origin = current_pos = (0, 0, 0)
max_distance = 0
for direction in read_input(DAY).readline().split(','):
	current_pos = move(current_pos, direction.strip())
	max_distance = max([max_distance, cube_distance(origin, current_pos)])


print(current_pos)
print(origin)
print(cube_distance(origin, current_pos))
print(max_distance)




#==============================================================================
end_terminal_block()