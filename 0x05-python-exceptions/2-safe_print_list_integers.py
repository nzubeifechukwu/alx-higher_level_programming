#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    '''Prints the first x integer elements of a list

    Args:
        my_list: list
        x: number of integer elements to print

    Return:
        Actual number of integers printed
    '''
    length = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            length = length + 1
        except (ValueError, TypeError):
            pass
    print()
    return length
