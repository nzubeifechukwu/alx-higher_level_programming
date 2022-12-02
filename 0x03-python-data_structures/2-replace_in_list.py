#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    '''Replaces an element of a list at a specific index

    Args:
        my_list: list
        idx: index of element to replace
        element: new element to replace element at index idx with

    Returns:
        new list with the new element
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
