#!/usr/bin/python3
'''Defines a square'''


class Square:
    '''Represents a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initializes the square

        Args:
            size: Size of the square. Defaults to 0
            position: Coordinates of the square. Defaults to (0, 0)

        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Gets the size

        Raises:
            TypeError: If size is not an integer
            ValueError: if size is less than 0

        '''
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        '''Gets the position of the square

        Raises:
            TypeError: If position is not a tuple of two positive integers

        '''
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for n in value:
            if n < 0 or type(n) is not int:
                message = 'position must be a tuple of 2 positive integers'
                raise TypeError(message)
        self.__position = value

    def area(self):
        '''Computes the area of the square

        Returns:
            Area of the square

        '''
        return (self.size ** 2)

    def my_print(self):
        '''Prints the square at the correct position using #'''
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(' ' * self.position[0], end='')
            for i in range(self.size):
                print('#', end='')
            print()
