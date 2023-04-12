#!/usr/bin/python3
"""This module teaches the a function to append file"""


def append_write(filename="", text=""):
    """Appends a string  using the 'a' keyword to the end of a UTF8 text file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
