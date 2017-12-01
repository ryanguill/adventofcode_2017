import sys
sys.path.append(sys.path[0] + "/..") #because python relative imports are weird...

from lib.utils import read_input, begin_terminal_block, end_terminal_block

DAY = '20157'
begin_terminal_block(DAY)


#print(read_input(DAY).read())



def test_foo():
	assert 1 == 1

def classify_line(line, state):
	
	(pre, suf) = line.strip('\n').split(' -> ')
	#if suf == 'a': print(line)
	if pre.isdigit():
		state[suf] = pre;
		return state
	else:
		parts = pre.split(' ')
		state[suf] = parts
		return state
	
def bit_and(x, y):
	return x & y

def bit_lshift(x, y):
	return x << y

def bit_rshift(x, y):
	return x >> y

def bit_or(x, y):
	return x | y

def bit_xor(x, y):
	return x ^ y

def bit_compl(x):
	return ~ x

opMapping = {
	"AND": bit_and,
	"LSHIFT": bit_lshift,
	"RSHIFT": bit_rshift,
	"OR": bit_or,
	"XOR": bit_xor
}

def memoize(f):
	memo = {}
	def helper(a, b, c):
		x = ':'.join(b)
		if x not in memo:            
			memo[x] = f(a, b, c)
		return memo[x]
	return helper
    
@memoize
def eval(state, statement, iter):
	iter += 1
	if iter >= 1000:
		return

	if not isinstance(statement, list):
		statement = [statement]

	print('eval', statement, len(statement), iter)

	if len(statement) == 1:
		if statement[0].isdigit():
			#print('isdigit', statement[0])
			print('!!!!!!!!!!!!!!!!!!!!', statement[0])
			return int(statement[0])
		else:
			#print('1f', statement[0], state[statement[0]])
			return eval(state, state[statement[0]], iter)
	elif len(statement) == 2:
		(op, a) = statement
		a = eval(state, a, iter)
		return bit_compl(a)

	elif len(statement) == 3:
		(a, op, b) = statement
		a = eval(state, a, iter)
		b = eval(state, b, iter)
		#print('3f', a, op, b)
		return opMapping[op](int(a), int(b))

state = {};

for line in read_input(DAY):
	state = classify_line(line, state)

state['b'] = ['16076']	


print('answer', eval(state, 'a', 0))

#print(list(state.keys()));
#print(state['a'])
#print(state)



end_terminal_block()	
