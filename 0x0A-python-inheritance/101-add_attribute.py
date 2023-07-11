#!/usr/bin/python3
"""Defines a function that adds attributes to objectst"""

def add_attribute(obj, att, value):
    """Add new attribute to an object if possible

    Args:
        obj (any): Object to add an attribute to
        att (str): Name of attribute to add to obj
        value (any): Value of att
    Raises:
        TypeError: If attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value
