#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""
import sys
from urllib import parse
from urllib import request


if __name__ == '__main__':
    adress = sys.argv[1]
    mail = sys.argv[2]
    mailcode = parse.urlencode({'email': mail})
    mailcode = mailcode.encode('utf-8')
    with request.urlopen(adress, mailcode) as response:
        print(response.read().decode('utf-8'))
