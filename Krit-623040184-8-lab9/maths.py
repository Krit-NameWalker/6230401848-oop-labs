def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError
    else:
        return a / b