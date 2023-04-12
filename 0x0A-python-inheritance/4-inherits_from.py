#!/usr/bin/python3
"""will check if the object is an instance of a class 
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of a class that IS inheritED otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)

