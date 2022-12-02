#!/usr/bin/python3
def element_at(my_list, idx):
    '''Retrieves element at a given index of a list

    Args:
        my_list: list
        idx: index

    Returns:
        element at given index
    '''
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list.pop(idx)
