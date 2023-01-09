#!/usr/bin/python3
'''This module is for a function that checks if:
    object is an instance of a specified class
    or an instance of a class that inherited from the specified class
'''


def is_kind_of_class(obj, a_class):
    '''Checks if an object is an instance of a specified class
        or an instance of a class that inherited from the specified class

    Args:
        obj: object
        a_class: specified class

    Returns:
        True if function description above is true
        False if not
    '''
    if isinstance(obj, a_class):
        return True
    return False
