#!/usr/bin/python3
'''A Rectangle class'''


class Rectangle:
    '''Represents a rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes a Rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height

    def __str__(self):
        '''Demonstrates how to print the rectangle'''
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            for j in range(self.width):
                rectangle += '#'
            rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        '''Returns a string representation of the rectangle'''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    @property
    def width(self):
        '''Gets and sets the width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
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
            TypeError: if height is not an integer
            ValueError: if height is less than 0
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
