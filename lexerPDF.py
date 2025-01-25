import ply.lex as lex

"""
Lexer for the PDF Compiler

Authoring: Keschubay Jun (base from TP4 corrections)
started and done: 10/12/2024
further edited to accomodate structure better: 25/01/2025
"""

reserved_words = ( 
 'for',
 'to',
 'if',
 #'else',
 'TEXT'
) 

tokens = (
	'NUMBER',
	'COMPARE_OP',
	'ADD_OP',
	'MUL_OP',
	'FIGURE_CMD',
	'COLOR', # for starters: only in HEX format (#FFFFFF)
	'IDENTIFIER',
	'CONTENT' # only recognises if wrapped in ""
) + tuple(s.upper() for s in reserved_words)

literals = '();=,{}'

def t_ADD_OP(t):
	r'[+-]'
	return t
	
def t_MUL_OP(t):
	r'[*/]'
	return t

def t_COMPARE_OP(t):
	r'(==|!=|>|<|>=|<=)'
	return t

def t_NUMBER(t):
	r'\d+(\.\d+)?'
	try:
		t.value = float(t.value)    
	except ValueError:
		print ("Line %d: Problem while parsing %s!" % (t.lineno,t.value))
		t.value = 0
	return t

def t_FIGURE_CMD(t):
	r'(LINE|TRIANGLE|CIRCLE)'
	return t

def t_CONTENT(t):
    r'".+"'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_words: 
        t.type = t.value.upper() 
    return t

def t_COLOR(t):
	r'\#[0-9|A-F|a-f]{6,6}'
	return t

t_ignore  = ' \t\n'

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
