#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0):
        '''Initializes the square

        Args:
            size: Size of the square. Defaults to 0

        '''
        self.size = size

    @property
    def size(self):
        '''Gets the size

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0

        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        '''Calculates area of the square'''
        return (self.size ** 2)

    def my_print(self):
        '''Prints square of size self.size using #'''
        if self.size == 0:
            print()
        for i in range(self.size):
            for i in range(self.size):
                print('#', end='')
            print()
