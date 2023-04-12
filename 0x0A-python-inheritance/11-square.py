#!/usr/bin/python3
"""module defines Rectangle subclass Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent the square"""

    def __init__(self, sizee):
        """Initializes the new square
        """
        self.integer_validator("size", sizee)
        super().__init__(size, sizee)
        self.__size = sizee
