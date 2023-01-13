#!/usr/bin/python3
'''Defines a Rectangle class that inherits from the Base class
'''
from models.base import Base


class Rectangle(Base):
    '''Represents a Rectangle class that inherits from the Base class

    Args:
        width: width of the Rectangle instance
        height: height of the Rectangle instance
        x: horizontal position of the Rectangle instance
        y: vertical position of the Rectangle instance
        id: id of the Rectangle instance
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        '''Demonstrates how to print the Rectangle instance
        '''
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height))

    @property
    def width(self):
        '''Gets and sets the width attributes

        Raises:
            TypeError: if value is not int
            ValueError: if value less than or equal to 0
        '''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Gets and sets the height attribute

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than or equal to 0
        '''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Gets and sets the attribute x

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        '''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Gets and sets the y attribute

        Raises:
            TypeError: if y is not int
            ValueError: if y is less than 0
        '''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Returns the area of the Rectangle instance
        '''
        return (self.width * self.height)

    def display(self):
        '''Prints the Rectangle instance in stdout with the character #
        '''
        position = ''
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()
