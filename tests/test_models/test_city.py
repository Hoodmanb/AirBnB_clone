#!/usr/bin/python3
"""Defines unittests for models/city.py.
Unittest classes:
    TestCity_instantiation
    TestCity_save
    TestCity_to_dict
"""

import unittest
import os
import sys
import models
from models.city import City

sys.path.append(os.path.abspath('.'))


class TestCity(unittest.TestCase):
    '''Test cases for City class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(City.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(City.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(City.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
