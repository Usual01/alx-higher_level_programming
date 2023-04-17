#!/usr/bin/python3
"""defines a LOCKED class"""


class LockedClass:
    """
    It Only allows instantiation of an attribute called first_name
    """

    __slots__ = ["first_name"]
