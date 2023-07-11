#!/usr/bin/python3
"""Defines p ython class-to-JSON function"""


def class_to_json(obj):
    """Return dictionary represntation of simple data structure"""
    return obj.__dict__
