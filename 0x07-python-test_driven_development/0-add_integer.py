#!/usr/bin/python3
"""This module defines the add integer function"""


def add_integer(a, b=98):
    """
    Args:
        a: first number
        b: second number
    Return:
        int: the sum a + b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
