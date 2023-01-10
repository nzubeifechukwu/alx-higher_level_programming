#!/usr/bin/python3
'''Defines a BaseGeometry class
'''


class BaseGeometry:
    '''Represents a BaseGeometry class
    '''
    def __init__(self):
        '''Instantiates the class
        '''
        pass

    def area(self):
        '''Computes the area of the BaseGeometry instance
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Validates dimensions of a BaseGeometry instance

        Args:
            name: name of the dimension
            value: value associated with the name

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to 0
        '''
        self.name = name
        if type(value) is not int:
            raise TypeError(self.name + ' must be an integer')
        if value <= 0:
            raise ValueError(self.name + ' must be greater than 0')
        self.value = value
