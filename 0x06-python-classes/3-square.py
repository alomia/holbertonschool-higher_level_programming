#!/usr/bin/python3
""" Square module """


class Square:
    def __init__(self, size=0):
        if type(size) == int:
            if size >= 0:
                self.__size__ = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ return area square by two"""
        return self.__size__ ** 2
