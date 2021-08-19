#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request

if __name__ == '__main__':
    requesto = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(requesto) as response:
        htmlbody = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(htmlbody)))
    print("\t- content: {}".format(htmlbody))
    print("\t- utf8 content: {}".format(htmlbody.decode('ascii')))
