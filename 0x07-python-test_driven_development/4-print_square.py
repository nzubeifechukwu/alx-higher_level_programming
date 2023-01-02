#!/usr/bin/python3
'''Prints a square of size <size> with the character #'''


def print_square(size):
    '''Prints a square with the character #

    Args:
        size: size of the square

    Raises:
        TypeError: if size not an int
        ValueError: if size less than 0
    '''
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
