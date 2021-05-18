#!/usr/bin/python3
"""Represents a Square"""


class Square:
    """It has an optional size attribute"""

    def __init__(self, size=0, position=(0, 0)):
        """This initializes the square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    def __repr__(self):
        str = ""
        if self.__size is 0:
            pass
        else:
            for ite in range(self.__position[1]):
                str += '\n'
            padding = ' ' * self.__position[0]
            square = '#' * self.size
            str += padding + square
            for ite in range(1, self.__size):
                str += '\n' + padding + square
        return str

    def area(self):
        """Return the area(size * size) of a square"""
        return self.__size ** 2

    def my_print(self):
        """Print our square using the # character"""
        if self.__size is not 0:
            for ite in range(self.__position[1]):
                print()
            for ite in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.size)
        else:
            print()

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

    @property
    def position(self):
        """This is a getter for the position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """This is a setter for the position of the square"""
        if type(position) is not tuple or len(position) is not 2\
           or type(position[0]) is not int or position[0] < 0\
           or type(position[1]) is not int or position[1] < 0:

            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = position
