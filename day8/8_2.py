import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...
from lib.utils import read_input, begin_terminal_block, end_terminal_block
from collections import defaultdict

DAY = 8

begin_terminal_block(DAY)
#==============================================================================




def do_op(registers, register, op, value):
	if op == '<':
		return registers[register] < value
	elif op == '>':
		return registers[register] > value
	elif op == '>=':
		return registers[register] >= value
	elif op == '<=':
		return registers[register] <= value
	elif op == '==':
		return registers[register] == value
	elif op == '!=':
		return registers[register] != value
	else:
		return False

max_value_ever = 0
registers = defaultdict(lambda: 0)

for line in read_input(DAY).readlines():
	register, op, delta, _, condition_register, comparison, comparison_value = line.split()

	#eval version that doesnt need the do_op()
	#if eval(str(registers[condition_register]) + comparison + str(comparison_value)):
	if do_op(registers, condition_register, comparison, int(comparison_value)):
		registers[register] += (int(delta) * (1 if op == 'inc' else -1))
		max_value_ever = max(max_value_ever, registers[register])

values = [registers[key] for key in registers]
print('max register at the end', max(values))
print('max ever', max_value_ever)




#==============================================================================
end_terminal_block()
