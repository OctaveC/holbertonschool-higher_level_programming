#!/usr/bin/python3
"""
Bonus Github exo
"""
import sys
import requests

if __name__ == '__main__':
    requesto = requests.get('https://api.github.com/repos/{}/{}/commits'
                            .format(sys.argv[2], sys.argv[1]))
    for commit in requesto.json()[0:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
