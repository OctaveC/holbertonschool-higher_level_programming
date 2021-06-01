#!/usr/bin/python3
""" Module for add_attribute """


def add_attribute(obj, attribute, value):
    """ Adds a new attribute to an object if it’s possible. """
    if hasattr(obj, "__dict__"):
            setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
