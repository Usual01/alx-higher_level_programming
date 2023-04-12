#!/usr/bin/python3
"""This module defines a text file-reading in utf-8"""


def read_file(filename=""):
    """writes the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
