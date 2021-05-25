#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter for the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width of the rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """ Returns a string representing our Rectangle instance """
        stringo = ""
        if self.__width is 0 or self.__height is 0:
            return stringo
        for ite in range(self.__height):
            stringo += "#" * self.__width + "\n"
        return stringo[:-1]

    def area(self):
        """ Returns the area of our Rectangle instance """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of our Rectangle instance """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2
