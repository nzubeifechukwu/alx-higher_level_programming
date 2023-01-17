#!/usr/bin/python3
'''Defines a Base class
'''
import json
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Returns the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None:
            return '[]'
        if type(list_dictionaries) is not list:
            raise TypeError('to_json_string argument must be a list of dicts')
        for obj in list_dictionaries:
            if type(obj) is not dict:
                raise TypeError('items in to_json_string arg must be dicts')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Writes the JSON string representation of list_objs to a file
        '''
        filename = cls.__name__ + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                # json.dump(list_dicts, f) achieves same thing as next line
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        '''Returns the list of JSON string representation
        '''
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Returns an instance with all attributes already set
        '''
        # Create a dummy Rectangle or Square instance
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances
        '''
        filename = cls.__name__ + '.json'
        if path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                json_string = f.read()
            list_dict = cls.from_json_string(json_string)
            return [cls.create(**d) for d in list_dict]
        return []
