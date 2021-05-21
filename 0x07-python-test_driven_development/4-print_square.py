#!/usr/bin/python3
"""
    This is a module that prints a square with the character #
"""


def print_square(size):
    """  Prints a square with the character # """

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for ite in range(size):
                print("#" * size)
