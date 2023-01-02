#!/usr/bin/python3
'''Adds two integers'''


def add_integer(a, b=98):
    '''Adds two integers

    Args:
        a: one integer
        b: another integer

    Return:
        a + b

    Raises:
        TypeError: if at least one of the inputs is not a number
    '''
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
