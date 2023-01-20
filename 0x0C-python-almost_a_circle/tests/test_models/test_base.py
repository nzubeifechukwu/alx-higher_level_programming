#!/usr/bin/python3
'''Unittest for Base class
'''
import unittest
from models.base import Base


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
        self.assertEqual(self.inst.id, 3)
        self.assertIs(type(self.inst.id), int)

    def test_instance_type(self):
        '''Tests if instance type is Base
        '''
        self.assertIs(type(self.inst), Base)

    def test_add_new_base(self):
        '''Tests if id is incremented when new instance is created
        '''
        new_inst = Base()
        self.assertEqual(new_inst.id, 2)

    def test_to_json_string(self):
        '''Tests to_json_string static method
        '''
        self.assertEqual(self.inst.to_json_string(None), '[]')
        self.assertEqual(self.inst.to_json_string([]), '[]')
        self.assertRaises(TypeError, self.inst.to_json_string, 1)
        self.assertRaises(TypeError, self.inst.to_json_string, [1])
