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
garbage_stream = []
chunk = []
garbage_chunk = []
idx = 0
garbage_flag = False
garbage_count = 0
while idx < len(stream):
	char = stream[idx]
	if char == '!':
		idx += 2
		continue

	if char == '<' and not garbage_flag: #gotta ignore it if were already in a garbage
		garbage_flag = True
		garbage_count += 1
		idx += 1
		#write out the chunk we've accumulated so far
		filtered_stream += chunk
		chunk = []
		continue

	if not garbage_flag:
		chunk.append(char)
	elif char == '>':
		garbage_flag = False
		garbage_stream += garbage_chunk
		garbage_chunk = []
		idx += 1
		continue
	else:
		garbage_chunk.append(char)
	idx += 1

print(len(garbage_stream))
#answer = 7053








#==============================================================================
end_terminal_block()