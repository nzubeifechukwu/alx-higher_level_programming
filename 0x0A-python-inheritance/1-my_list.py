#!/usr/bin/python3
'''This module defines a class MyList that inherits from the list object
'''


class MyList(list):
    '''Represents a MyList class that inherits from the list object
    '''

    def __init__(self):
        '''Instantiates a MyList class
        '''
        super().__init__()

    def print_sorted(self):
        '''Prints the MyList instance in ascending order
        '''
        print(sorted(self))
