#!/usr/bin/python3
'''A Rectangle class'''


class Rectangle:
    '''Represents a Rectangle'''

    def __init__(self, width=0, height=0):
        '''Instantiates the rectangle

        Args:
            width: Width of the rectangle. Defaults to 0.
            height: Height of the rectangle. Defaults to 0.
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets and sets the width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Gets and sets the height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Computes the area of the rectangle'''
        return (self.width * self.height)

    def perimeter(self):
        '''Computes the perimeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return (2*self.width + 2*self.height)
