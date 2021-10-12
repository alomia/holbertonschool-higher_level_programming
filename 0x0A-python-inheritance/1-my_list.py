#!/usr/bin/python3
"""This module contains a function that returns a list object"""


class MyList(list):
    """class MyList"""

    def print_sorted(self):
        """
        MyList class subclass of list
        Attributes:
        print_sorted: prints the list in a sorted fashion
        """
        print(sorted(self))
