#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import urllib.request

if __name__ == '__main__':
    adress = sys.argv[1]
    with urllib.request.urlopen(adress) as answer:
        print(answer.getheader('X-Request-Id'))
