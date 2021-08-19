#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib import parse
from urllib import request
from urllib import error


if __name__ == '__main__':
    adress = sys.argv[1]
    try:
        with request.urlopen(adress) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as errornum:
        print("Error code: {}".format(errornum.code))
