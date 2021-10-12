#!/usr/bin/python3
"""
    function that writes a string to a text file
"""


def append_write(filename="", text=""):
    """
    Arg:
        filename: name of file
        text: string of file
    Return: len string
    """
    with open(filename, 'a', encoding='utf-8') as f:
        w = f.write(text)
        return w
