#!/usr/bin/python3
""" create new class """


class Rectangle:
    '''initialize the class'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """rectangle width"""
        return self.__width

    @property
    def height(self):
        """rectangle width"""
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        strg = ""
        h = self.__height
        if self.__width != 0 and self.height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    strg = strg + "#"
                if i != x - 1:
                    strg = strg + "\n"
        return strg
