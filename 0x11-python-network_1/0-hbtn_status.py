#!/usr/bin/python3
""" Script which fetches url"""


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as rep:
        dev = rep.read()
        print("Body reponse:")
        print("\t- type: {}".format(type(dev)))
        print("\t- content: {}".format(dev))
        print("\t- utf8 content: {}".format(dev.decode('utf-8')))
