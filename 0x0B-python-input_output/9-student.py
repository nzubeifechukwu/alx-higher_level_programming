#!/usr/bin/python3
'''Defines a Student class
'''


class Student:
    '''Represents a Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''Instantiates a Student object

        Args:
            first_name: first name of the student instance
            last_name: last name of the student instance
            age: age of the student instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns a dictionary representation of a Student instance
        '''
        dict_rep = {}
        for a in dir(self):
            if not a.startswith('__'):
                if type(getattr(self, a)) in [list, dict, str, int, bool]:
                    dict_rep[a] = getattr(self, a)
        return dict_rep
