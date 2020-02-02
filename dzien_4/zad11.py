def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b:
        return a/b


def eval(string):   #1+2, 3/5
    a, op, b= string.spil()
    operations = {
        "+":add,
        "-":sub,
        "*":mul,
        "/":div
    }
    operation = operations[op]
    return operation(a,b)