#!/usr/bin/python3
"""Defines unittests for models/review.py.
Unittest classes:
    TestReview_instantiation
    TestReview_save
    TestReview_to_dict
"""
import unittest
import os
import sys
from models.review import Review

sys.path.append(os.path.abspath('.'))


class TestReview(unittest.TestCase):
    '''Test cases for Review class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(Review.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(Review.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_init(self):
        '''Test initialization'''
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
