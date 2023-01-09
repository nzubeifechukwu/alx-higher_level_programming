#!/usr/bin/python3
'''Defines a Rectangle class that inherits from the BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Represents a Rectangle class that inherits from the BaseGeometry class
    '''
    def __init__(self, width, height):
        '''Instantiates a Rectangle class

        Args:
            width: width of the rectangle
            height: height of the rectangle

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is not greater than 0
        '''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
