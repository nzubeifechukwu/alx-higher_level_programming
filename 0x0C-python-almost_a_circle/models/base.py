#!/usr/bin/python3
'''Defines a Base class
'''


class Base:
    '''Represents a base class

    Attributes:
        __nb_objects: holds the number of Base instances created
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Instantiates a Base object

        Args:
            id: type int. Defaults to None
        '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
