#!/usr/bin/python3
"""
Return a Pascal's Triangle
"""


def append_after(filename="", search_string="", new_string=""):
    """Return a triangle"""
    txt = ""
    with open(filename, "r") as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string

    with open(filename, "w") as w:
        w.write(txt)
