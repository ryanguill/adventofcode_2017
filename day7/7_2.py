import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle
from collections import Counter


DAY = 7

begin_terminal_block(DAY)
#==============================================================================
"""
0 weight
1 children
2 children_weight
"""


def calculate_weight(towers, base):
	tower = towers[base]
	weight = tower[0] + sum([calculate_weight(towers, prog) for prog in tower[1]])
	towers[base] = (tower[0], tower[1], weight)
	return weight

def find_anomaly(towers, base):
	tower = towers[base]

	children = tower[1]
	if len(children) == 0:
		return False

	child_weights = [(child, calculate_weight(towers, child)) for child in children]
	weights = [weight for (_, weight) in child_weights]
	if len(set(weights)) > 1:
		(most_common, _), (least_common, _) = Counter(weights).most_common()
		diff = least_common - most_common
		if diff != 0:
			oddball = [t for t in child_weights if t[1] == least_common][0]
			#print('oddball:', oddball, 'diff:', diff)

			has_sub_oddball = find_anomaly(towers, oddball[0])
			if not has_sub_oddball:
				print('answer >>', towers[oddball[0]][0] - diff)
			return True
	else:
		return False



towers = {}
for line in read_input(DAY).readlines():
	tower = tuple(line.split())
	base = tower[0]
	weight = tower[1].strip('()')
	held_up = [x.strip(',') for x in tower[3:]]

	towers[base] = (int(weight), held_up)

base = 'veboyvy'


find_anomaly(towers, base)


#==============================================================================
end_terminal_block()