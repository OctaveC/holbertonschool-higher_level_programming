#!/usr/bin/python3
""" Module for save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file. """
    with open(filename, "w", encoding="utf-8") as opening:
        json.dump(my_obj, opening)
