#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    requesto = requests.get("https://api.github.com/user",
                            auth=(sys.argv[1], sys.argv[2]))
    print(requesto.json().get("id"))
