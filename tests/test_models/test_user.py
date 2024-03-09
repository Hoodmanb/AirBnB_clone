#!/usr/bin/python3
"""Defines unittests for models/user.py.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
import os
import sys
from models.user import User

sys.path.append(os.path.abspath('.'))

class TestUser(unittest.TestCase):
    '''Test cases for User class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(User.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(User.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(User.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

if __name__ == '__main__':
    unittest.main()
