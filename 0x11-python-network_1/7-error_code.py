#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests


if __name__ == '__main__':
    adress = sys.argv[1]
    requesto = requests.get(adress)

    if requesto.status_code > 400:
        print("Error code: {}".format(requesto.status_code))
    else:
        print("{}".format(requesto.text))
