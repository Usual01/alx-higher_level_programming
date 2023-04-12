#!/usr/bin/python3
"""This module defines a function for text file insertion"""


def append_after(files="", search="", string=""):
    """Inserts text after each line \n  containing a given string in a file
    """
    text = ""
    with open(files) as newfile:
        for line in newfile:
            text = text + line
            if searched in line:
                text = text + string
    with open(filename, "w") as files:
        files.write(text)
