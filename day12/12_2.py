import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle
from collections import defaultdict

DAY = 12

begin_terminal_block(DAY)
#==============================================================================

connections = defaultdict(set)

for line in read_input(DAY).readlines():
	source, destinations = line.split('<->')
	source = int(source.strip())
	for dest in map(int, set(destinations.strip().split(', '))):
		connections[source].add(dest)
		connections[dest].add(source)

#print(connections)
#print(len(connections))

seen = set()
groups = 0
for start in range(len(connections)):
	#if we have already came across this number, no need to look at it again
	if start in seen:
		continue

	groups += 1

	to_process = [start]
	while len(to_process):
		source = to_process.pop()
		for dest in connections[source]:
			if dest not in seen:
				seen.add(dest)
				to_process.append(dest)

print(groups)

#==============================================================================
end_terminal_block()