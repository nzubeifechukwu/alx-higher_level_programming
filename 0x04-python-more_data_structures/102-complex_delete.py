#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''Deletes keys with a specific value in a dictionary

    Args:
        a_dictionary: dictionary
        value: value of some keys in the dictionary
    Return:
        dictionary with all keys having the given value deleted
    '''
    keys_to_del = []

    for k, v in a_dictionary.items():
        if v == value:
            keys_to_del.append(k)

    for k in keys_to_del:
        del a_dictionary[k]

    return a_dictionary
