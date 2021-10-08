#!/usr/bin/python3
"""Module to print a square"""


def print_square(size):
    """
    Args: size: size of the square
    Returns:
        print square
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end='')
            i, j
        print("")
