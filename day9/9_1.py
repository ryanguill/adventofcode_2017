import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle

DAY = 9

begin_terminal_block(DAY)
#==============================================================================

#neutralize all garbage first
#then count open and closes for the groups

stream = []
#read it all in so we can look ahead and behind
for char in read_input(DAY).read():
	stream.append(char)


filtered_stream = []
chunk = []
idx = 0
garbage_flag = False
while idx < len(stream):
	char = stream[idx]
	if char == '!':
		idx += 2
		continue

	if char == '<':
		garbage_flag = True
		idx += 1
		#write out the chunk weve accumulated so far
		filtered_stream += chunk
		chunk = []
		continue

	if not garbage_flag:
		chunk.append(char)
	elif char == '>':
		garbage_flag = False
		idx += 1
		continue
	idx += 1

print(len(stream))
print(len(filtered_stream))

#testing
#filtered_stream = [char for char in '{{{},{},{{}}}}']

#print(filtered_stream)

score = 0
layer = 0
for char in filtered_stream:

	if char == '{':
		layer += 1
		score += layer
	elif char == '}':
		layer -= 1

	print(char)
	print(layer)
	print(score)
	print()

print(score)













#==============================================================================
end_terminal_block()