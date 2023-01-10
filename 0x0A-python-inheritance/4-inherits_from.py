#!/usr/bin/python3
'''This module contains a function that checks if an object is an instance of
    a class inherited (directly or indirectly) from a specified class
'''


def inherits_from(obj, a_class):
    '''Checks if an object is an instance of a class directly or indirectly
        inherited from a specified class

    Args:
        obj: object
        a_class: specified class

    Returns:
        True if the above function description is true
        False otherwise
    '''
    return (isinstance(obj, a_class) != (type(obj) is a_class))
