import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block, hash_sha1
from itertools import cycle

DAY = 6

begin_terminal_block(DAY)
#==============================================================================

def configuration_hash(bucket_list):
	return hash_sha1((':').join(list(map(str, bucket_list))))

for line in read_input(DAY).readlines():
	buckets = list(map(int, line.split()))

observed_configurations = set()
observed_configurations.add(configuration_hash(buckets))

number_of_buckets = len(buckets)

iterations = 0
while True:
	iterations += 1
	#print(buckets)
	mx = max(buckets)
	#print(mx)
	idx = next(i for i, v in enumerate(buckets) if v == mx)
	#print(idx)

	# clear out the register in this index
	buckets[idx] = 0

	for _, idx in zip(\
		range(0, mx), \
		cycle([x for x in range(idx + 1, number_of_buckets)] + [x for x in range(0, idx + 1)])):
		buckets[idx] += 1

	hsh = configuration_hash(buckets)
	if hsh in observed_configurations:
		break

	observed_configurations.add(hsh)


print(iterations)

#==============================================================================
end_terminal_block()
