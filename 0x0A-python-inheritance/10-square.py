#!/usr/bin/python3
'''Defines a Square class that inherits from the Rectangle class
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents a Square class that inherits from the Rectangle class
    '''

    def __init__(self, size):
        '''Instantiates a square object

        Args:
            size: size of the square
        '''
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        '''Demonstrates how to describe the square instance
        '''
        return '[Rectangle] {}/{}'.format(self.__size, self.__size)

    def area(self):
        '''Computes the area of the square
        '''
        return (self.__size**2)
