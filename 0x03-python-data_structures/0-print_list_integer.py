#!/usr/bin/python3
def print_list_integer(my_list=[]):
    '''prints integers in a list

    Arg:
        my_list: a list of integers
    '''
    for n in my_list:
        print('{:d}'.format(n))
