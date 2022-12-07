#!/usr/bin/python3
def best_score(a_dictionary):
    '''Finds a key with biggest integer value in a dictionary

    Arg:
        a_dictionary: dictionary

    Return:
        key of with biggest int value
    '''
    max_v = 0
    if not isinstance(a_dictionary, dict):
        return None
    for k, v in a_dictionary.items():
        if v > max_v:
            max_v = v
            max_k = k
    return max_k
