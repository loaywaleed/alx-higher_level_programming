#!/usr/bin/python3
"""
Python module
adds two numbers
returns result
"""


def add_integer(a, b=98):
    """Adds two integers
    Args:
        a, b: numbers to add
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
