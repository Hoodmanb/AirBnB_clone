#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import unittest
import os
import sys
from models.amenity import Amenity

sys.path.append(os.path.abspath('.'))


class TestAmenity(unittest.TestCase):
    '''Test cases for Amenity class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(Amenity.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(Amenity.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
