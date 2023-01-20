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

    def test_instance_type(self):
        '''Tests that the class instance is of type Base
        '''
        self.assertIs(type(self.inst), Base)

    def test_id(self):
        '''Tests if id attribute is of type int
        '''
        self.assertIs(type(self.inst.id), int)
        self.assertEqual(self.inst.id, 1)

    def test_to_json_string(self):
        '''Tests to_json_string static method
        '''
        self.assertEqual(self.inst.to_json_string(None), '[]')
        self.assertEqual(self.inst.to_json_string([]), '[]')
        self.assertRaises(TypeError, self.inst.to_json_string, 1)
        self.assertRaises(TypeError, self.inst.to_json_string, [1])
