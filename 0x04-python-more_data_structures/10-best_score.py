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

    keys = list(a_dictionary)
    values = list(a_dictionary.values())
    max_v = values[0]

    for i, v in enumerate(values):
        if v > max_v:
            max_v = v
            max_k = keys[i]

    return max_k
