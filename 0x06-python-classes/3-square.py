#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0):
        '''Initializes the square

        Args:
            size: size of the square
            Must be an integer not less than 0

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0

        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''Computes the area of the square

        Returns:
            area of the square

        '''
        return (self.__size ** 2)
