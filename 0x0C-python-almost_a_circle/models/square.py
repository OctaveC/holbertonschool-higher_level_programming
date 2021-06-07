#!/usr/bin/python3
""" Module for Square Class """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Square Class inheriting from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print a formated reresentation opf our Rectangle """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Reassigns our Square """
        if args:
            argnum = len(args)
            if argnum >= 1:
                self.id = args[0]
            if argnum >= 2:
                self.width = args[1]
                self.height = args[1]
            if argnum >= 3:
                self.x = args[2]
            if argnum >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of Square """
        return {"id": self.id, "size": self.width,
               "x": self.x, "y": self.y}

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter for size """
        self.width = size
        self.height = size
