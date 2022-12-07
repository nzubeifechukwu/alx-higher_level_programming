#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    '''Multiply all items of a list with using loops

    Args:
        my_list: list
        number: multiplier

    Return:
        Copy of my_list but with each item multiplied by number
    '''
    return list(map(lambda x: x * number, my_list))
