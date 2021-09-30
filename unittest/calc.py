# calc.py
# source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Unit-Testing/calc.py
# youtube: https://www.youtube.com/watch?v=6tNS--WetLI

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y