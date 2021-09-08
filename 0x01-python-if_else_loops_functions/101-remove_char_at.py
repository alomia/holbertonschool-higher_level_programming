#!/usr/bin/python3
def remove_char_at(str, n):
    if n > 0:
        strcp = str[:n] + str[(n + 1):]
        return strcp
    return str
