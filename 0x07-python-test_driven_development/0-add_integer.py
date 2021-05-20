#!/usr/bin/python3
"""
    This is a module that adds integers and/or floats
"""


def add_integer(a, b=98):
    """ Adds two integers/floats """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
