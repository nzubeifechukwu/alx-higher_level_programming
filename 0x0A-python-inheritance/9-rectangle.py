#!/usr/bin/python3
'''Defines a Rectangle class that inherits from the BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a Rectangle class that inherits from the BaseGeometry class
    '''
    def __init__(self, width, height):
        '''Instantiates a Rectangle object

        Args:
            width: width of the rectangle
            height: height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is not positive
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        '''Demonstrates how to describe the rectangle insance
        '''
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)

    def area(self):
        '''Computes the area of the rectangle
        '''
        return (self.__width * self.__height)
