#!/usr/bin/python3
""" Module for Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class inheriting from BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Return the area of our Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ Returns informal information about our Rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
