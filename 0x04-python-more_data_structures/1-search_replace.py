#!/usr/bin/python3
def search_replace(my_list, search, replace):
    '''Replaces all occurrences of an item in a list by another in a new list

    Args:
        my_list: list
        search: elements to replace
        replace: new element to replace search

    Return:
        New list with all occurrences of search replaced by replace
    '''
    return list(map(lambda x: replace if x == search else x, my_list))
