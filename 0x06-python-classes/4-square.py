#!/usr/bin/python3
"""Represents a Square"""


class Square:
    """It has an optional size attribute"""

    def __init__(self, size=0):
        """This initializes the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the area(size * size) of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """This is a getter for the size of the square"""
        return self.__size

    @size.setter
    def size(self, size):
        """This is a setter for the size of the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
