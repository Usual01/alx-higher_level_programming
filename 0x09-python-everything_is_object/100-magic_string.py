#!/usr/bin/python3
def magic_string():
    magic_string = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string - 1) + "BestSchool")
