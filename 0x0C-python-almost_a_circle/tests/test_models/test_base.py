#!/usr/bin/python3
'''Unittest for Base class
'''
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    '''Tests the Base class and its associated methods and attributes
    '''

    def setUp(self):
        '''Initializes conditions for all test methods
        '''
        b = Base()

    def test_instance_type(self):
        '''Tests that the class instance is of type Base
        '''
        self.assertIs(type(b), Base)

    def test_id_int(self):
        '''Tests if id attribute is of type int
        '''
        self.assertIs(type(b.id), int)

    def test_to_json_string(self):
        '''Tests to_json_string static method
        '''
        self.assertEqual(b.to_json_string(None), '[]')
        self.assertEqual(b.to_json_string([]), '[]')
        self.assertRaises(TypeError, b.to_json_string, 1)
        self.assertRaises(TypeError, b.to_json_string, [1])
