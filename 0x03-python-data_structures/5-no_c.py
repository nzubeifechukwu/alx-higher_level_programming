#!/usr/bin/python3
def no_c(my_string):
    '''removes all characters c and C from a string

    Args:
        my_string: string

    Returns:
        new string with no c or C
    '''
    my_list = []
    for c in my_string:
        if c != 'c' and c != 'C':
            my_list.append(c)
    return ''.join(my_list)
