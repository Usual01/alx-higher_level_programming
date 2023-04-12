#!/usr/bin/python3
"""This module for Student class"""


class Student:
    """Represent a student class ."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr = None):
        """makes a key pair dictionary-like representation of the Student.
        If attr is a list of strings, represents only those attributes included in the list
        """
        if (type(attr) == list and
                all(type(element) == str for element in attr)):
            return {i: getattr(self, i) for i in attr if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student
        """
        for i, j in json.items():
            setattr(self, i, j)
