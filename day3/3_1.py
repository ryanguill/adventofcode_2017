import math
import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, manhattan_distance

DAY = 3

begin_terminal_block(DAY)
#==============================================================================

puzzle_input = 347991

def fn(n):
	layer = math.ceil(math.sqrt(n))
	length_of_side = layer if layer % 2 != 0 else layer + 1
	steps_to_center_from_corner = (length_of_side - 1) / 2
	cycle = n - ((length_of_side - 2) ** 2)
	distance_from_prev_diagonal = cycle % (length_of_side - 1)
	answer = steps_to_center_from_corner + \
		abs(distance_from_prev_diagonal - \
		steps_to_center_from_corner)
	return answer


print(fn(puzzle_input))

#==============================================================================
end_terminal_block()
