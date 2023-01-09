#!/usr/bin/python3
'''Defines a MyInt class that inherits from int
'''


class MyInt(int):
    '''Represents a MyInt class that inherits from int
    '''

    def __init__(self, other):
        super().__init__()

    def __eq__(self, other):
        '''Compares if two instances of MyInt are equal
            Inverts the == operator
        '''
        return not super().__eq__(other)

    def __ne__(self, other):
        '''Checks if two instances of MyInt are not equal
            Inverts the != operator
        '''
        return not super().__ne__(other)
