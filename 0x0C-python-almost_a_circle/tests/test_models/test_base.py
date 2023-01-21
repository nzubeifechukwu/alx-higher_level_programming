#!/usr/bin/python3
'''Unittest for Base class
'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    '''Tests the Base class and its associated methods and attributes
    '''

    def setUp(self):
        '''Initializes variable before each test method is run
        '''
        self.inst = Base()

    def tearDown(self):
        '''Deletes the variable after each test method is run
        '''
        del self.inst

    def test_id(self):
        '''Tests for value and type of id attribute
        '''
        self.assertEqual(self.inst.id, 1)
        self.assertIs(type(self.inst.id), int)

    def test_instance_type(self):
        '''Tests if instance type is Base
        '''
        self.assertIs(type(self.inst), Base)

    def test_new_instance(self):
        '''Tests if id is incremented when new instance is created
        '''
        new_inst = Base()
        self.assertEqual(new_inst.id, new_inst.id)

    def test_new_instance_with_id(self):
        '''Tests if id is set when new instance is created with an id
        '''
        new_inst = Base(23)
        self.assertEqual(new_inst.id, 23)

    def test_to_json_string(self):
        '''Tests to_json_string static method
        '''
        self.assertEqual(self.inst.to_json_string(None), '[]')
        self.assertEqual(self.inst.to_json_string([]), '[]')
        self.assertEqual(self.inst.to_json_string([{'id': 1}]), '[{"id": 1}]')
        with self.assertRaises(TypeError):
            self.inst.to_json_string(1)
        with self.assertRaises(TypeError):
            self.inst.to_json_string([1])

    def test_save_to_file(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([Rectangle(2, 3)])
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(Rectangle(2, 3))
