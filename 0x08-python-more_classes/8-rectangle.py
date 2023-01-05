#!/usr/bin/python3
'''A Rectangle class'''


class Rectangle:
    '''Represents a Rectangle'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        '''Initializes a rectangle instance

        Args:
            width: width of the rectangle
            height: height of the rectangle
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        '''Demonstrates how to print the rectangle'''
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            rectangle += '\n'
        return rectangle[:-1]

    def __repr__(self):
        '''Returns a string representation of the rectangle'''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        '''Destroys the rectangle'''
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        '''Gets and sets the width of the rectangle

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

    def area(self):
        '''Computes the area of the rectangle'''
        return (self.width * self.height)

    def perimeter(self):
        '''Computes the perimeter of the rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        return (2*self.width + 2*self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Compares two rectangles based on their areas

        Returns:
            The bigger of the two rectangles, or rect_1 if they are equal

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle instance
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
