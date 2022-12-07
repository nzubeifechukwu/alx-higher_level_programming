#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    '''Replaces or adds key/value in a dictionary

    Args:
        a_dictionary: dictionary
        key: key to add or replace
        value: value of key

    Returns:
        New dictionary with key/value replaced or added
    '''
    a_dictionary[key] = value
    return a_dictionary
