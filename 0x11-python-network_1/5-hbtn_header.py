#!/usr/bin/python3
"""script that takes in URL, sends request to URL"""

from sys import argv
import requests

if __name__ == '__main__':
    y = requests.get(argv[1])
    print(y.headers.get('X-Request-Id'))
