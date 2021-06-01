#!/usr/bin/python3
""" module for is_same_class """


def is_same_class(obj, a_class):
    """ returns True if the object is exactly instance of specified class """
    return a_class is type(obj)
