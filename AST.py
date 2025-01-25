import operator

OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    ">": operator.gt,
    "<=": operator.le,
    ">=": operator.ge,
}


class Node:
    type = "Node"

    def __init__(self, *children):
        self.children = children

    def asciitree(self, prefix=""):
        result = f"{prefix}{self!r}\n"
        prefix += "|  "
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
INTERFACER: "utils.interfacer.Interfacer" = None


def save_all_children_decorator(init):
    def decorated_init(self, *children):
        self.children = children
        init(self, *children)

    return decorated_init


class ProgramNode(Node):
    def execute(self):
        for statement in self.children:
            statement.execute()


class ForNode(Node):
    @save_all_children_decorator
    def __init__(self, var, start, end, program):
        self.var = var
        self.start = start
        self.end = end
        self.program = program

    def execute(self):
        for i in range(int(self.start.execute()), int(self.end.execute()) + 1):
            vars[self.var] = i
            self.program.execute()
        del vars[self.var]  # cleans iterator


class IfNode(Node):
    @save_all_children_decorator
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def execute(self):
        if self.condition.execute():
            ##print(f'IF succeded, {self.condition = }, {self.condition.execute()}')
            self.body.execute()


class TokenNode(Node):
    @save_all_children_decorator
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
    @save_all_children_decorator
    def __init__(self, operation, op1, op2):
        self.operation = operation
        self.op1 = op1
        self.op2 = op2

    def execute(self):
        return float(
            OPERATIONS[self.operation](
                self.op1.execute(),
                self.op2.execute(),
            )
        )


class AssignNode(Node):
    @save_all_children_decorator
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def execute(self):
        vars[self.var] = self.expr.execute()


class FigureCmdNode(Node):
    @save_all_children_decorator
    def __init__(self, figure_type, color, positionX, positionY, size):
        self.figure_type = figure_type
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
        self.size = size

    def execute(self):
        pos_x = self.positionX.execute()
        pos_y = self.positionY.execute()
        size = self.size.execute()

        INTERFACER.setColor(self.color, self.color)
        halfsize = size // 2

        if self.figure_type == "LINE":
            A = [pos_x - halfsize, pos_y]
            B = [pos_x + halfsize, pos_y]
            INTERFACER.drawLine([*A, *B])

        elif self.figure_type == "CIRCLE":
            INTERFACER.drawCircle([pos_x, pos_y], size)

        elif self.figure_type == "TRIANGLE":
            A = [pos_x - halfsize, pos_y - halfsize]
            B = [pos_x + halfsize, pos_y - halfsize]
            C = [pos_x, pos_y + halfsize]
            INTERFACER.drawTriangle(A, B, C)

        else:
            print("Error: Unrecognised figure type")


class TextNode(Node):
    @save_all_children_decorator
    def __init__(self, color, positionX, positionY, size, content):
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
        self.size = size
        self.content = content

    def execute(self):
        pos_x = self.positionX.execute()
        pos_y = self.positionY.execute()
        size = self.size.execute()

        INTERFACER.setColor(None, None, self.color)
        INTERFACER.drawText(
            [pos_x, pos_y],
            content=self.content,
            size=size,
        )


class NoopNode(Node):
    def execute(self):
        pass
