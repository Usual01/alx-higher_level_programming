#!/usr/bin/python3
"""defines a Python class-JSON function"""


def class_to_json(obj):
    """dictionary representation of a data structure"""
    return obj.__dict__
