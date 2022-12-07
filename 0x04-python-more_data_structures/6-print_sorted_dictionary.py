#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Prints a dictionary by ordered keys

    Arg:
        a_dictionary: dictionary
    '''
    for k in sorted(a_dictionary):
        print('{}: {}'.format(k, a_dictionary[k]))
