#!/usr/bin/python3
""" Module for Square that inherits from Rectangle """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square Class inheriting from Rectangle """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
