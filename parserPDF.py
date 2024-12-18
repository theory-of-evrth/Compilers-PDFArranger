import ply.yacc as yacc

from lexerPDF import tokens 


"""
TODO: treatment of numbers, variables, cycles

statement - > elementcreation
structure - > for
"""

operations = {
    '+' : lambda x,y : x+y,
    '-' : lambda x,y : x-y,
    '*' : lambda x,y : x*y,
    '/' : lambda x,y : x/y
}

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('left', 'OPEN_PAR'),
)

def p_expression_op(p):
    '''
    expression : expression ADD_OP expression 
    | expression MUL_OP expression
    '''
    p[0]=operations[p[2]](p[1],p[3])

def p_parentheses(p):
    '''
    expression : OPEN_PAR expression CLOSE_PAR
    '''
    p[0]=p[2]

def p_error(p):
    print("Syntax error in line %d" % p.lineno)
    yacc.errok()



yacc.yacc(outputdir='/generated')

if __name__ == "__main__":
    import sys 

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=True)
    print(result)