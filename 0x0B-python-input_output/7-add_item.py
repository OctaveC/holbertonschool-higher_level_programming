#!/usr/bin/python3
""" Script that add all arguments to Python list, and then save them to file"""
import sys
import json

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    listo = load("add_item.json")
except FileNotFoundError or ValueError:
    listo = []
save(listo + sys.argv[1:], "add_item.json")
