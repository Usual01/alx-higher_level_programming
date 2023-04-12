#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int"""


class MyInt(int):
    """Inverts the int operators ==(equals to) and !=(not equals to) """

    def __eq__(self, val):
        """changes the == operathor with != behavior"""
        return self.real != val

    def __ne__(self, val):
        """Overrides != operathor with == behavior"""
        return self.real == val
