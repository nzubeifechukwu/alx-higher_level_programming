#!/usr/bin/python3
def max_integer(my_list=[]):
    '''finds the biggest integer of a list

    Args:
        my_list: list

    Returns:
        biggest integer
    '''
    if len(my_list) == 0:
        return None

    max_n = my_list[0]

    for n in my_list:
        if n > max_n:
            max_n = n

    return max_n
