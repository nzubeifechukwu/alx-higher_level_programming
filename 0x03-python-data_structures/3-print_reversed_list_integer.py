#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    '''Prints all integers of a list in reverse

    Arg:
        my_list: list
    '''
    my_list.reverse()
    for n in my_list:
        print('{:d}'.format(n))
