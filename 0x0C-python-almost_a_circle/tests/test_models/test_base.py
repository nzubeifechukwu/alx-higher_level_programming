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
        self.inst = Base()

    def test_instance_type(self):
        '''Tests that the class instance is of type Base
        '''
        self.assertIs(type(self.inst), Base)

    def test_id_int(self):
        '''Tests if id attribute is of type int
        '''
        self.assertIs(type(self.inst.id), int)

    def test_to_json_string(self):
        '''Tests to_json_string static method
        '''
        self.assertEqual(self.inst.to_json_string(None), '[]')
        self.assertEqual(self.inst.to_json_string([]), '[]')
        self.assertRaises(TypeError, self.inst.to_json_string, 1)
        self.assertRaises(TypeError, self.inst.to_json_string, [1])
