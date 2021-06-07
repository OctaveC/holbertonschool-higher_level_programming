#!/usr/bin/python3
""" Module for Rectangle Class """
from .base import Base


class Rectangle(Base):
    """ Rectangle Class inheriting from Base """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """ Print a formated reresentation opf our Rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Reassigns our Rectangle """
        if args:
            argnum = len(args)
            if argnum >= 1:
                self.id = args[0]
            if argnum >= 2:
                self.width = args[1]
            if argnum >= 3:
                self.height = args[2]
            if argnum >= 4:
                self.x = args[3]
            if argnum >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """ Returns the area of our Rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints a visual representation of our Rectangle instance """
        for y in range(self.__y):
            print()
        for height in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def to_dictionary(self):
        """ Returns the dictionary representation of our Rectangle """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    def validates_int(self, value, name):
        """ Checks that an int is valid """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0 and (name is "x" or name is "y"):
            raise ValueError("{} must be >= 0".format(name))
        if value <= 0 and (name is "width" or name is "height"):
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for width """
        self.validates_int(width, "width")
        self.__width = width

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter for height """
        self.validates_int(height, "height")
        self.__height = height

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter for x """
        self.validates_int(x, "x")
        self.__x = x

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter for y """
        self.validates_int(y, "y")
        self.__y = y
