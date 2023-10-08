#!/usr/bin/python3
"""takes in URL, sends a request to URL and displays"""

import requests
from sys import argv

if __name__ == '__main__':
    y = requests.get(argv[1])
    status = y.status_code
    print(y.text) if status < 400 else print(
        "Error code: {}".format(y.status_code))
