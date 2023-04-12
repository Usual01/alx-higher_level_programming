#!/usr/bin/python3
"""class Rectangle that inherits from the BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represents a rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new rectangle"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the print() and str() representation of a Rectangle"""
        word = "[" + str(self.__class__.__name__) + "] "
        word = word + str(self.__width) + "/" + str(self.__height)
        return word
