#!/usr/bin/python3
"""
Contains lookup function
"""


def lookup(obj):
    """returns list of available attributes and methods of the object"""
    return dir(obj)
