#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list

    Args:
        my_list: list
        x: number of elements to print

    Return:
        Actual number of elements printed
    '''
    length = 0

    for i in range(x):
        try:
            print(my_list[i], end='')
            length = length + 1
        except IndexError:
            break
    print()
    return length
