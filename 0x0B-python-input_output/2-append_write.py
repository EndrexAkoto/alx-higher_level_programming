#!/usr/bin/python3
"""Defines file-appending function"""


def append_write(filename="", text=""):
    """Appends string to the end of UTF8 text file

    Args:
        filename (str): Name of file to append to
        text (str): String appended to the file
    Returns:
        Number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
