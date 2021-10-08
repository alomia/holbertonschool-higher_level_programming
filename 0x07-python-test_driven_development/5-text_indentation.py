#!/usr/bin/python3
"""module defines the text_indentation function"""


def text_indentation(text):
    """
    Args:
        text: text to print
    """
    x = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if x == 1 and i is ' ':
            print('', end='')
            x = 0
            continue
        if i is '.' or i is '?' or i is ':':
            print("{}\n". format(i))
            x = 1
        else:
            print(i, end='')
            x = 0
