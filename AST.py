import functools
import operator

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge,
}

class Node:
    type = 'Node'
    def __init__(self, *children):
        self.children = children

    def asciitree(self, prefix=''):
        result = f"{prefix}{self!r}\n"
        prefix += '|  '
        for child in self.children:
            if not isinstance(child, Node):
                result += f"{prefix} {type(child)!r}: {child!r}\n"
            else:
                result += child.asciitree(prefix)
        return result
    
    def __str__(self):
        return self.asciitree()
    
    def __repr__(self):
        return type(self).__name__

vars = {}

class ProgramNode(Node):
    def execute(self):
        for statement in self.children:
            statement.execute()

class ForNode(Node):
    def __init__(self, var, start, end, program):
        self.var = var
        self.start = start
        self.end = end
        self.program = program

    def execute(self):
        for i in range(self.start, self.end + 1):
            vars[self.var] = i
            self.program.execute()
        del vars[self.var] # cleans iterator

class IfNode(Node):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def execute(self):
        if self.condition.execute():
            self.body.execute()

class TokenNode(Node):
    def __init__(self, token):
        self.token = token

    def execute(self):
        if isinstance(self.token, str):
            try:
                return vars[self.token]
            except KeyError:
                print(f"Error: variable {self.token} is undefined!")
        return self.token

class OpNode(Node):
    def __init__(self, operation, *operands):
        self.operation = operation
        self.operands = operands

    def execute(self):
        args = [expr.execute() for expr in self.operands]
        if len(args) == 1:
            args = [0] + args
        result = functools.reduce(operations[self.operation], args)
        return float(result)

class AssignNode(Node):
    
    def execute(self):
        vars[self.children[0].tok] = self.children[1].execute()

class FigureCmdNode(Node):
    # TODO : call interfacer to draw figure
    ...

class TextNode(Node):
    # TODO : call interfacer to draw text
    pass