#!/usr/bin/python3
"""
This module defines a rectangle
"""


class Rectangle:
    """
    This class defines a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def __str__(self):
        """ Returns a string representing our Rectangle instance """
        stringo = ""
        for ite in range(self.__height):
            stringo += str(self.print_symbol) * self.__width + "\n"
        return stringo[:-1]

    def __repr__(self):
        """ Returns a formal description of our Rectangle instance """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Returns a message when our rectangle is killed """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """ Returns the area of our Rectangle instance """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns the perimeter of our Rectangle instance """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width + self.__height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the biggest Rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
