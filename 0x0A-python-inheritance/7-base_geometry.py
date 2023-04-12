#!/usr/bin/python3
"""base geometry of class BaseGeometry"""


class BaseGeometry:
    """this class represents the base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, val):
        """validates a value as an integer
        """
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if val <= 0:
            raise ValueError("{} must be greater than 0".format(name))
