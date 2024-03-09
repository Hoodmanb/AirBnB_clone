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
from models.place import Place

sys.path.append(os.path.abspath('.'))


class TestPlace(unittest.TestCase):
    '''Test cases for Place class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(Place.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(Place.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
