import ply.lex as lex

"""
Lexer for the PDF Compiler

Authoring: Keschubay Jun (base from TP4 corrections)
started: 10/12/2024

"""

reserved_words = ( 
 'for',
 'LINE',
 'TEXT',
 'CIRCLE',
 'TRIANGLE' 
) 

tokens = (
	'NUMBER',
	'ADD_OP',
	'MUL_OP',
	'COLOR', # for starters: only in HEX format (#FFFFFF)
	'IDENTIFIER',
	'CONTENT' # only recognises if in ""
) + tuple(map(lambda s:s.upper(),reserved_words)) 

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

def t_CONTENT(t):
	# to figure out how to include spec. symbols: https://stackoverflow.com/questions/18057962/regex-pattern-including-all-special-characters
	r'"[A-Za-z_0-9 \p{P}\p{S}]+"'
	return t

def t_IDENTIFIER(t):
    r'[A-Za-z_]\w*'
    if t.value in reserved_words: 
        t.type = t.value.upper() 
    return t



def t_COLOR(t):
	r'\#[0-9|A-F|a-f]{5,5}'
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
