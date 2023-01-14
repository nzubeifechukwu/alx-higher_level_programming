#!/usr/bin/python3
'''Defines a Square class that inherits from a Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Represents a Square class that inherits from the Rectangle class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiates a Square object

        Args:
            size: size of the Square instance
            x: coordinate of the Square instance on the horizontal axis
            y: coordinate of the Square instance on the vertical axis
            id: id of the Square instance
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Demonstrates how to print the Square instance
        '''
        return '[Square] ({}) {}/{} - {}'.format(
                self.id, self.x, self.y, self.height)

    @property
    def size(self):
        '''Gets and sets the size attribute

        Raises:
            TypeError: if size is not int
            ValueError: if size is not positive
        '''
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, *kwargs):
        '''Updates the attributes of the Square instance
        '''
        attributes = list(vars(self).keys())
        if bool(args):  # args exists and is not empty
            for i in len(args):
                vars(self)[attributes[i]] = args[i]
        else:
            for k, v in vars(self).items():

