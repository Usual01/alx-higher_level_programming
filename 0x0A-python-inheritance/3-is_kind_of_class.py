#!/usr/bin/python3
"""checks if  an instance of a vlass exists in the defined class"""

    def is_kind_of_class(obj, a_class):
        """Check if an object is an instance or inherited instance of a class.
        arguments: the object to be checked and the type(a_class)
        returns true if object is sn inherited instance otherwise 
        """
        if isinstance(obj, a_class):
            return True
        return False

