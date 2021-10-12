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
        new_list = self[:]
        for i in range(len(new_list) - 1):
            if new_list[i] > new_list[i + 1]:
                temp = new_list[i + 1]
                new_list[i + 1] = new_list[i]
                new_list[i] = temp
        print(new_list)
