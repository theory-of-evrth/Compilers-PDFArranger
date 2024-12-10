import ply.lex as lex

"""
TODO : treat eligible tokens, find suitable regex
"""

tokens = (
	'NUMBER',
	'ADD_OP',
	'MUL_OP',
	'COLOR', # for starters: only in HEX format (#FFFFFF)
	'IDENTIFIER',
	'CONTENT' # only recognises if in ""
)

literals = '();='

def t_ADD_OP(t):
	r'[+-]'
	return t
	
def t_MUL_OP(t):
	r'[*/]'
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	try:
		t.value = float(t.value)    
	except ValueError:
		print ("Line %d: Problem while parsing %s!" % (t.lineno,t.value))
		t.value = 0
	return t

def t_COLOR(t):
	r''
	return t

def t_IDENTIFIER(t):
	r'[A-Za-z_]\w*'
	return t

def t_CONTENT(t):
	r''
	return t
	
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
	print ("Illegal character '%s'" % repr(t.value[0]))
	t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
	import sys
	prog = open(sys.argv[1]).read()

	lex.input(prog)

	while 1:
		tok = lex.token()
		if not tok: break
		print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))  #type: ignore
