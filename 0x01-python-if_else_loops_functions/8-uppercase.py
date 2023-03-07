#!/usr/bin/python3
# isupper: A function that prints strings in upper character
# str: string to change
# Returns: capitalized string


def uppercase(str):
    for c in str:
        if ord(c) >= 65 and ord(c) <= 90:
        	print("{}".format(c), end="")
    print("")
