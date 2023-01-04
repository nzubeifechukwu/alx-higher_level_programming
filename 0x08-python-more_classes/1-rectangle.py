#!/usr/bin/python3
'''A Rectangle class'''


class Rectangle:
    '''Represens a Rectangle'''

    def __init__(self, width=0, height=0):
        '''Instantiates the rectangle

        Args:
            width: width of the rectangle. Defaults to 0
            height: height of the rectangle. Defaults to 0
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets and sets the width attribute

        Raises:
            TypeError: if width not an int
            ValueError: if with less than 0
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
        '''Gets and sets the height of the rectangle

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
