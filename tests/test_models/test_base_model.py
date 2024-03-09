#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import unittest
import os
import sys
from datetime import datetime
from models.base_model import BaseModel

sys.path.append(os.path.abspath('.'))


class TestBaseModel(unittest.TestCase):
    '''Test cases for BaseModel class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(BaseModel.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(BaseModel.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_init(self):
        '''Test initialization'''
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        '''Test __str__ method'''
        model = BaseModel()
        self.assertEqual(str(model), f"BaseModel
                         ({model.id}) {model.__dict__}")

    def test_save(self):
        '''Test save method'''
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        '''Test to_dict method'''
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict[
            '__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
