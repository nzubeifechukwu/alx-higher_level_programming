#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Multiplies all values of a dictionary by 2

    Args:
        a_dictionary: dictionary

    Return:
        A copy of a_dictionary but with all values multiplied by 2
    '''
    return {k: v * 2 for k, v in a_dictionary.items()}
