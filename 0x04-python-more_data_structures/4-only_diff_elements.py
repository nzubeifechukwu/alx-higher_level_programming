#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    '''Returns set of all elements present in only set

    Args:
        set_1: set
        set_2: set

    Returns:
        Set of all elements present in only set
    '''
    return set_1 ^ set_2
