#!/usr/bin/python3
"""represents a class Student"""


class Student:
    """Represensts a student class."""

    def __init__(self, first_name, last_name, age):
        """Initializes the new Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """makes a dictionary representation of the Student"""
        return self.__dict__
