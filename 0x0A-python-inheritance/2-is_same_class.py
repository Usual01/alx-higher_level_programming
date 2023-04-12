#!/usr/bin/python3
"""chexks a class if a function is present"""


    def is_same_class(obj, a_class):
        """The methof returns true is a duplicate is found
        arguments: the object, the copied type/instance (a_class)
        Returns true if it finds instance otherwise false
        """
        if type(obj) == a_class:
            return True
        return False

