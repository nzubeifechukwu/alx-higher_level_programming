#!/usr/bin/python3
'''Returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''Gets the list of available attributes and methods of an object

    Args:
        obj: the object

    Returns:
        list of available attributes and methods of obj
    '''
    return dir(obj)
