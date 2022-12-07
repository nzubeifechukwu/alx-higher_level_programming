#!/usr/bin/python3
def best_score(a_dictionary):
    '''Finds a key with biggest integer value in a dictionary

    Arg:
        a_dictionary: dictionary

    Return:
        key of with biggest int value
    '''
    if not isinstance(a_dictionary, dict):
        return None
    return max(a_dictionary)
