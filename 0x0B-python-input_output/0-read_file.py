#!/usr/bin/python3
"""
    that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename: name of file
    """


    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


