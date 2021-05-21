#!/usr/bin/python3
"""
    This is a module that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ This function indents text based on special characters """

    if type(text) is not str:
        raise TypeError("text must be a string")
    leap = True
    for char in text:
        if not (char is ' ' and leap is True):
            print(char, end="")
            leap = False
            if char in [':', '.', '?']:
                print()
                print()
                leap = True
