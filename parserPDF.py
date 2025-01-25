import ply.yacc as yacc

from lexerPDF import tokens 
import AST

"""
TODO: treatment of numbers, variables, cycles, conditions

statement - > elementcreation
structure - > for
"""

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MUL_OP'),
    ('right', 'UMINUS'),
)

def p_program_input(p):
    ''' program : statement '''
    p[0] = AST.ProgramNode(p[1])

def p_program_continuation(p):
    ''' program : statement ';' program '''
    p[0] = AST.ProgramNode(p[1], *p[3].children) 

def p_statement_assignment(p):
    ''' statement : IDENTIFIER '=' expression '''
    p[0] = AST.AssignNode(p[1], p[3])

def p_statement_drawing_figurecmd(p):
    ''' statement : FIGURE_CMD COLOR '(' expression ',' expression ')' expression '''
    p[0] = AST.FigureCmdNode(p[1], p[2], p[4], p[6], p[8])

def p_statement_drawing_TEXT(p):
    ''' statement : TEXT COLOR '(' expression ',' expression ')' expression CONTENT '''
    p[0] = AST.TextNode(p[2], p[4], p[6], p[8], p[9])

def p_for_structure(p):
    ''' statement : FOR IDENTIFIER '=' expression TO expression '{' program '}' '''
    p[0] = AST.ForNode(p[2], p[4], p[6], p[8])

def p_if_structure(p):
    ''' statement : IF expression '{' program '}' '''
    p[0] = AST.IfNode(p[2], p[4])

def p_expression_op(p):
    '''
    expression : expression ADD_OP expression 
               | expression MUL_OP expression
               | expression COMPARE_OP expression
    '''
    p[0] = AST.OpNode(p[2], p[1], p[3])

def p_expression_num_or_var(p): 
    ''' expression : NUMBER
                   | IDENTIFIER ''' 
    p[0] = AST.TokenNode(p[1]) 
 
def p_minus(p): 
    ''' expression : ADD_OP expression %prec UMINUS''' 
    p[0] = AST.OpNode(p[1], p[2]) 

def p_parentheses(p):
    ''' expression : '(' expression ')' '''
    p[0] = p[2]

def p_error(p):
    print("Syntax error in line %d" % p.lineno)
    yacc.errok()


yacc.yacc(outputdir='/generated')

if __name__ == "__main__":
    import sys 

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=True)
    print(result)