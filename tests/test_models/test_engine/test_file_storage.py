#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import unittest
import os
import sys
import json
from models.file_storage import FileStorage
from models.base_model import BaseModel

sys.path.append(os.path.abspath('.'))


class TestFileStorage(unittest.TestCase):
    '''Test cases for FileStorage class'''

    def test_documentation_module(self):
        '''Test documentation for the module'''
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation_class(self):
        '''Test documentation for the class'''
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation_methods(self):
        '''Test documentation for the methods'''
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all(self):
        '''Test all method'''
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        '''Test new method'''
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        all_objects = storage.all()
        self.assertIn(f"BaseModel.{model.id}", all_objects)

    def test_save_reload(self):
        '''Test save and reload methods'''
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        storage.reload()
        all_objects = storage.all()
        self.assertIn(f"BaseModel.{model.id}", all_objects)


if __name__ == '__main__':
    unittest.main()
