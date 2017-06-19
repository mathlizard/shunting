import operator


def shunting(s):
    """ evaluate s ~ assume that s is well-formed: i.e. ( ( 3 + 5 ) * ( 3 - 1 ) ) """
    switch = { '+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv }
    operator_stack = []
    output = []
    l = s.split()
    for c in l:
        if c.isdigit():
            output.append(int(c))
        elif c in '+-*/':
            operator_stack.append(c)
        elif c is ')':
            x = output.pop()
            y = output.pop()
            o = operator_stack.pop()
            output.append(switch[o](y, x))
    return output[-1]
