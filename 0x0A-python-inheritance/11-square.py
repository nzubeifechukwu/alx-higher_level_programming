#!/usr/bin/python3
'''Defines a Square class that inherits from a Rectangle class
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Represents a Square class that inherits from a Rectangle class
    '''

    def __init__(self, size):
        '''Instantiates the class

        Args:
            size: size of the square instance
        '''
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        '''Demonstrates how to describe a square instance
        '''
        return '[Square] {}/{}'.format(self.__size, self.__size)

    def area(self):
        '''Computes the area of the square instance
        '''
        return (self.__size**2)
