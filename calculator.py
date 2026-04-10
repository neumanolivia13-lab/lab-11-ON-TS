def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def logarithm(x, base):
    if x <= 0:
        raise ValueError("Invalid argument")
    if base <= 0 or base == 1:
        raise ValueError("Invalid base")
    return math.log(x, base)


def exp(x):
    return math.exp(x)
