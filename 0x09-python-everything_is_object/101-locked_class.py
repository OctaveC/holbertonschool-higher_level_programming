#!/usr/bin/python3
""" Module containing the LockedClass class """
class LockedClass:
    """ Class that prevents the user from creating new instance attributes, """
    """ except if the new instance attribute is called first_name. """
    __slots__ = "first_name"
