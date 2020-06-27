# This script is in the public-domain.
# You can do whatever you want with it :)

from lark import *

l = Lark(
'''

?entail: [[equiv] "|=" [LOGIC " "]] equiv
?equiv:  impl ("<->" equiv)*
?impl:   or   ("->" impl)*
?or:     and  ("|" or)*
?and:    (neg | atom) ("&" and)*
neg:     "~" (neg | atom)
?atom:   VAR | T | F | I | N | B | ("(" equiv ")")

T: "T" | "1"
F: "F" | "0"
I: "I" | "U"
N: "N"
B: "B"
VAR: ("a".."z")+
LOGIC: "CPL"i | "K3"i | "B3"i | "L3"i | "LP"i | "RM3"i | "FDE"i

%ignore " "

''', start='entail')


logics = {

	# Classical propositional logic - boolean logic that we all know and love
	'CPL': {
		'values': ['0', '1'],
		'designated': {'1'},	
		'neg': {
			'0':'1',
			'1':'0'
		},	
		'and': {
			'0': { '0':'0', '1':'0' },
			'1': { '0':'0', '1':'1' },
		},	
		'or': {
			'0': { '0':'0', '1':'1' },
			'1': { '0':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', '1':'1' },
			'1': { '0':'0', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', '1':'0' },
			'1': { '0':'0', '1':'1' },
		}
	},
	
	# Kleen's strong 3-valued logic
	'K3': {
		'values': ['0', 'i', '1'],
		'designated': {'1'},
		'neg': {
			'0':'1',
			'i':'i',
			'1':'0'
		},
		'and': {
			'0': { '0':'0', 'i':'0', '1':'0' },
			'i': { '0':'0', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'1', 'i':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'i':'1', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'i':'i', '1':'0' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		}
	},
	
	# Bochvar's internal 3-valued logic
	'B3': {
		'values': ['0', 'i', '1'],
		'designated': {'1'},
		'neg': {
			'0':'1',
			'i':'i',
			'1':'0'
		},
		'and': {
			'0': { '0':'0', 'i':'i', '1':'0' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'1', 'i':'i', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'i':'i', '1':'0' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		}
	},
	
	# Lukasiewicz's 3-valued logic
	'L3': {
		'values': ['0', 'i', '1'],
		'designated': {'1'},
		'neg': {
			'0':'1',
			'i':'i',
			'1':'0'
		},
		'and': {
			'0': { '0':'0', 'i':'0', '1':'0' },
			'i': { '0':'0', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'1', 'i':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'i':'1', '1':'1' },
			'i': { '0':'i', 'i':'1', '1':'1' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'i':'i', '1':'0' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		}
	},
	
	# Priest's logic of paradox (LP)
	'LP': {
		'values': ['0', 'i', '1'],
		'designated': {'1', 'i'},
		'neg': {
			'0':'1',
			'i':'i',
			'1':'0'
		},
		'and': {
			'0': { '0':'0', 'i':'0', '1':'0' },
			'i': { '0':'0', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'1', 'i':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'i':'1', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'i':'i', '1':'0' },
			'i': { '0':'i', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		}
	},
	
	# Mix 3-valued logic
	'RM3': {
		'values': ['0', 'i', '1'],
		'designated': {'1', 'i'},
		'neg': {
			'0':'1',
			'i':'i',
			'1':'0'
		},
		'and': {
			'0': { '0':'0', 'i':'0', '1':'0' },
			'i': { '0':'0', 'i':'i', '1':'i' },
			'1': { '0':'0', 'i':'i', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'i':'i', '1':'1' },
			'i': { '0':'i', 'i':'i', '1':'1' },
			'1': { '0':'1', 'i':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'i':'1', '1':'1' },
			'i': { '0':'0', 'i':'i', '1':'1' },
			'1': { '0':'0', 'i':'0', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'i':'0', '1':'0' },
			'i': { '0':'0', 'i':'i', '1':'0' },
			'1': { '0':'0', 'i':'0', '1':'1' },
		}
	},
	
	# First degree entailment - Belnap logic (B4)
	'FDE': {
		'values': ['0', 'n', 'b', '1'],
		'designated': {'1', 'b'},
		'neg': {
			'0':'1',
			'n':'n',
			'b':'b',
			'1':'0'
		},	
		'and': {
			'0': { '0':'0', 'n':'0', 'b':'0', '1':'0' },
			'n': { '0':'0', 'n':'n', 'b':'0', '1':'n' },
			'b': { '0':'0', 'n':'0', 'b':'b', '1':'b' },
			'1': { '0':'0', 'n':'n', 'b':'b', '1':'1' },
		},
		'or': {
			'0': { '0':'0', 'n':'n', 'b':'b', '1':'1' },
			'n': { '0':'n', 'n':'n', 'b':'1', '1':'1' },
			'b': { '0':'b', 'n':'1', 'b':'b', '1':'1' },
			'1': { '0':'1', 'n':'1', 'b':'1', '1':'1' },
		},
		'impl': {
			'0': { '0':'1', 'n':'1', 'b':'1', '1':'1' },
			'n': { '0':'n', 'n':'n', 'b':'1', '1':'1' },
			'b': { '0':'b', 'n':'1', 'b':'b', '1':'1' },
			'1': { '0':'1', 'n':'n', 'b':'b', '1':'1' },
		},
		'equiv': {
			'0': { '0':'1', 'n':'n', 'b':'b', '1':'0' },
			'n': { '0':'n', 'n':'n', 'b':'1', '1':'n' },
			'b': { '0':'b', 'n':'1', 'b':'b', '1':'b' },
			'1': { '0':'0', 'n':'n', 'b':'b', '1':'1' },
		}
	},
}
			
			
def find_vars(t, var_vals):
	if type(t) == Token:
		if t.type == 'VAR':
			var_vals[t] = '0'
	elif type(t) == Tree:
		for child in t.children:
			find_vars(child, var_vals)
			
			
def find_logic_type(t):
	if t.data == 'entail':
		for child in t.children:
			if type(child) == Token and child.type == 'LOGIC':
				return str(child)
	return 'CPL'



def tree_to_string(t):
	if type(t) == Token:
		return str(t)
		
	c = [tree_to_string(child) for child in t.children]
		
	if t.data == 'neg':
		return '~' + c[0]
	
	elif t.data == 'entail':
		if len(c) == 3:
			return '%s |=%s %s' % (c[0], c[1], c[2])
		elif len(c) == 2:
			if type(t.children[0]) == Token and t.children[0].type == 'LOGIC':
				return '|=%s %s' % (c[0], c[1])
			else:
				return '%s |= %s' % (c[0], c[1])
				
	else:
		if t.data == 'and':
			return '(%s & %s)' % (c[0], c[1])
		elif t.data == 'or':
			return '(%s | %s)' % (c[0], c[1])
		elif t.data == 'impl':
			return '(%s -> %s)' % (c[0], c[1])
		elif t.data == 'equiv':
			return '(%s <-> %s)' % (c[0], c[1])
	
	
def assign_truth_vals(t, var_vals, node_vals, logic):
	
	# check if we already found the truth value of this branch
	if t in node_vals:
		return node_vals[t]
		
	if type(t) == Token:
		if t.type == 'VAR':
			node_vals[t] = var_vals[t]
		elif t.type == 'T':
			node_vals[t] = '1'
		elif t.type == 'B':
			node_vals[t] = 'b'
		elif t.type == 'I':
			node_vals[t] = 'i'
		elif t.type == 'N':
			node_vals[t] = 'n'
		elif t.type == 'F':
			node_vals[t] = '0'
		else:
			node_vals[t] = '0'
		return node_vals[t]
	
	c = [assign_truth_vals(child, var_vals, node_vals, logic) for child in t.children]
	
	if t.data == 'entail':
		designated = logic['designated']
		if len(c) == 2:
			if type(t.children[0]) == Token and t.children[0].type == 'LOGIC':
				node_vals[t] = c[1]
			else:
				node_vals[t] = '1' if (not c[0] in designated) or c[1] in designated else '0'
		elif len(c) == 3:
			node_vals[t] = '1' if (not c[0] in designated) or c[2] in designated else '0'
	elif t.data == 'neg':
		node_vals[t] = logic['neg'][c[0]]
	elif t.data == 'and' or t.data == 'or' or t.data == 'impl' or t.data == 'equiv':
		node_vals[t] = logic[str(t.data)][c[0]][c[1]]

	return node_vals[t]
	
	
def truth_to_string(t, node_vals):
	if type(t) == Token:
		if t.type == 'LOGIC':
			return ' ' * len(t)
		else:
			return node_vals[t]
		
	c = [truth_to_string(child, node_vals) for child in t.children]
	myval = node_vals[t]
		
	if t.data == 'neg':
		return node_vals[t] + c[0]
	
	elif t.data == 'entail':
		if len(c) == 3:
			return '%s  %s%s %s' % (c[0], myval, c[1], c[2])
		elif len(c) == 2:
			if type(t.children[0]) == Token and t.children[0].type == 'LOGIC':
				return ' %s%s %s' % (myval, c[0], c[1])
			else:
				return '%s  %s %s' % (c[0], myval, c[1])
				
	else:
		if t.data == 'and':
			return ' %s %s %s ' % (c[0], myval, c[1])
		elif t.data == 'or':
			return ' %s %s %s ' % (c[0], myval, c[1])
		elif t.data == 'impl':
			return ' %s %s  %s ' % (c[0], myval, c[1])
		elif t.data == 'equiv':
			return ' %s  %s  %s ' % (c[0], myval, c[1])
			
			
def help():
	print('')
	print('supported logics')
	print('  CPL      classic propositional logic (default)')
	print('  K3       Kleen\'s 3-valued logic')
	print('  B3       Bochvar\'s internal 3-valued logic')
	print('  LP       Priest\'s logic of paradox')
	print('  L3       Lukasiewicz\'s 3-valued logic')
	print('  RM3      mix 3-valued logic')
	print('  FDE      Belnap 4-valued logic, first degree entailment')
	print('')
	print('operator syntax')
	print('  ~p       not')
	print('  p & q    and')
	print('  p | q    or')
	print('  p -> q   implication: ~p | q')
	print('  p <-> q  equivalence: (p -> q) & (q -> p)')
	print('')
	print('atom syntax')
	print('  p        variable: sequence of lowercase characters')
	print('  1/T      true')
	print('  0/F      false')
	print('  I/U      unspecified: for 3-valued logic')
	print('  B        both true and false: for 4-valued logic')
	print('  N        neither true nor false: for 4-valued logic')
	print('')
	print('entailment syntax')
	print('  p |= q   entailment in classical propositional logic (CPL)')
	print('  p |=L q  entailment in logic "L"')
	print('  |= p     tautology in classical propositional logic (CPL)')
	print('  |=L p    tautology in logic "L"')
	print('           note that "L" must be one of the supported logics above')
	print('')
	print('examples')
	print('  > ~(p & q) |= ~p | ~q')
	print('  > ~p | q |=K3 p -> q')
	print('  > p -> (q -> (p -> q))')
	print('')
	
	
def main():
	print('')
	print(' truth table generator for multi-valued logic')
	print(' ............................................')
	print(' input a formula into the prompt')
	print(' "help" for reference, "quit" to quit')
	print('')
	
	while True:
		expression = input('> ').strip()
		if expression == 'quit' or expression == 'exit':
			break
		elif expression == 'help':
			help()
			continue
		
		try:
			tree = l.parse(expression)
		except Exception as e:
			print('\n' + str(e))
			continue
		
		logic = logics[find_logic_type(tree).upper()]
		
		var_vals = {}
		find_vars(tree, var_vals)
	
		tree_str = '  ' + tree_to_string(tree)
		print('\n' + tree_str)
		print('.' * (len(tree_str) + 2))
		
		always_valid = True
		invalid_rows = []
		no_error = True
		
		V = logic['values']
		# generating all permuations of possible variable assignments using integer
		for val in range(len(V)**len(var_vals)):
			node_vals = {}
			
			vals = val
			for var in reversed(list(var_vals)):
				var_vals[var] = V[vals % len(V)]
				vals //= len(V)
			
			try:
				holds = assign_truth_vals(tree, var_vals, node_vals, logic)
				if holds != '1':
					always_valid = False
					invalid_rows += [val + 1]
				
				valid_str = '* ' if holds != '1' else '  '
				print(valid_str + truth_to_string(tree, node_vals))
			except:
				print('error')
				no_error = False
				break
			
		if no_error: 
			print('')
			if (tree.data == 'entail'):
				if always_valid:
					print('entailment always holds')
				else:
					print('entailment doesn\'t hold in row(s) ' + ','.join(str(x) for x in invalid_rows))
			else:
				if always_valid:
					print('formula is a tautology')
				else:
					print('formula is not a tautology, in row(s) ' + ','.join(str(x) for x in invalid_rows))
		print('')
				
			
if __name__ == '__main__':
	main()