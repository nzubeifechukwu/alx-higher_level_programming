#!/usr/bin/python3
'''Unittest for max_integer([...])
'''

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''Tests for the max_integer function
    '''
    def test_inputs(self):
        '''Check different kinds of inputs'''
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer((1, 2, 3)), 3)
        self.assertEqual(max_integer('school'), 's')

    def test_types(self):
        '''Raise type errors when necessary'''
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, 2)
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, [1, None, 3])
        self.assertRaises(TypeError, max_integer, [1, 'school', 2])
        self.assertRaises(TypeError, max_integer, [1, [1, 2], 2])

    def test_keys(self):
        '''Raise key errors when necessary'''
        self.assertRaises(KeyError, max_integer, {'name': 'Nzube'})
