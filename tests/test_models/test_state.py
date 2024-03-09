#!/usr/bin/python3
"""Defines unittests for models/state.py.
Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import unittest
import os
import sys
from models.state import State

sys.path.append(os.path.abspath('.'))


class TestState(unittest.TestCase):
    '''Test cases for State class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(State.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(State.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(State.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
