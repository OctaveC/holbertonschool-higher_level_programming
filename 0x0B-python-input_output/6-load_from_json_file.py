#!/usr/bin/python3
""" Module for load_from_json_file """
import json


def load_from_json_file(filename):
    """ Writes an Object to a text file. """
    with open(filename, encoding="utf-8") as opening:
        return json.load(opening)
