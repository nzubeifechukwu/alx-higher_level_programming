#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    '''deletes item at a given index in a list

    Args:
        my_list: list to delete its item
        idx: index of the item

    Return:
        New list with item deleted
    '''
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
