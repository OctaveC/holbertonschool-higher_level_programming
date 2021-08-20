#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    requesto = requests.post("http://0.0.0.0:5000/search_user", {"q": letter})

    try:
        data = requesto.json()
        if len(data) != 0:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
