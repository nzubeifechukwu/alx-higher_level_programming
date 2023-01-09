#!/usr/bin/python3
'''This module checks if an object is exactly an instance of a specified class
'''


def is_same_class(obj, a_class):
    '''Checks if an object is exactly an instance of a given class

    Args:
        obj: object
        a_class: given class

    Returns:
        True if obj is exactly an instance of a_class
        False otherwise
    '''
    if type(obj) is a_class:
        return True
    return False
