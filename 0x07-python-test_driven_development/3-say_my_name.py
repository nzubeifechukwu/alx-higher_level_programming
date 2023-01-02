#!/usr/bin/python3
'''Prints: My name is <first name> <last name>

Where <first name> and <last name> must be strings

'''


def say_my_name(first_name, last_name=''):
    '''Prints the string: My name is <first name> <last name>

    Args:
        first_name: string
        last_name: string. Defaults to an empty string

    Raises:
        TypeError: if first_name or last_name is not a string
    '''
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')

    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
