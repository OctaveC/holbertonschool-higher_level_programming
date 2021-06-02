#!/usr/bin/python3
""" Module for append_after """


def append_after(filename="", search_string="", new_string=""):
    """ Inserts a line of text to a file, """
    """ after each line containing a specific string. """
    mod = ""
    with open(filename, "r+", encoding="utf-8") as opening:
        texte = opening.readlines()
        for ligne in texte:
            mod += ligne
            if search_string in ligne:
                mod += new_string
        opening.write(mod)
