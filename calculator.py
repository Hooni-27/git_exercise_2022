# Calculator (function = Add, Sub, Mul, Div)
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return 0

def square(a):
    return a*a
