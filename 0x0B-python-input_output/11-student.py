#!/usr/bin/python3
'''Defines a Student class
'''


class Student:
    '''Represents a Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''Instantiates a Student object
        Args:
            first_name: first name of a Student instance
            last_name: last name of a Student instance
            age: age of a Student instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns the dict representation of a Student instance
        '''
        dict_rep = {}
        ser = [list, dict, str, int, bool]
        if type(attrs) is not list:
            for a in dir(self):
                if not a.startswith('__') and type(getattr(self, a)) in ser:
                    dict_rep[a] = getattr(self, a)
        else:
            if all(type(a) is str for a in attrs):
                for a in attrs:
                    if not a.startswith('__') and a in dir(self):
                        dict_rep[a] = getattr(self, a)
        return dict_rep

    def reload_from_json(self, json):
        '''Replaces all attributes of a Student instance

        Args:
            json: dict repr of all public attributes of a Student instance
        '''
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
