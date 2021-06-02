#!/usr/bin/python3
""" Module for append_write """


def append_write(filename="", text=""):
    """ Appends a string to a text file (UTF8). """
    with open(filename, "a", encoding="utf-8") as opening:
        opening.write(text)
    return len(text)
