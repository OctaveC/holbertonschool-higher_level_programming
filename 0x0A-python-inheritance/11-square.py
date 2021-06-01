#!/usr/bin/python3
""" Module for Square that inherits from Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square Class inheriting from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
