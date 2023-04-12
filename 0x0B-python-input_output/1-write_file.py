#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """Opens and writes a string to a text file and closes with 'WITH' KEYWORD
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
