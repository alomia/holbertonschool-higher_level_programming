#!/usr/bin/python3
"""
Return a Pascal's Triangle
"""


def append_after(filename="", search_string="", new_string=""):
    """Return a triangle"""
	acumulado = ""
	with open(filename, "r") as f:
		for line in f:
			acumulado += line
			if search_string in line:
          acumulado += new_string
		
	with open(filename, "w") as w:
		w.write(acumulado)
