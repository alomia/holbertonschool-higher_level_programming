#!/usr/bin/python3
"""This module defines the function say_my_name"""


def say_my_name(first_name, last_name=""):
    """
    Arg:
        first_name: saves the first name
        last_name: saves the last name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
