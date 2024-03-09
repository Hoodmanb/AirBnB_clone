#!/usr/bin/python3

"""
Defines unittests for console.py.
Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""

import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand

sys.path.append(os.path.abspath('.'))


class TestHBNBCommand(unittest.TestCase):
    '''Test cases for HBNBCommand class'''

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        '''Test help command'''
        with patch('builtins.input', side_effect=['help', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn('Documented commands (type help <topic>):', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        '''Test create command'''
        with patch('builtins.input', side_effect=['create BaseModel', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertNotEqual(output, '')

    def test_quit(self):
        '''Test quit command'''
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('builtins.input', return_value='quit'):
                HBNBCommand().cmdloop()
                output = mock_stdout.getvalue()
                self.assertEqual(output, '')

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        '''Test show command'''
        with patch('builtins.input',
                   side_effect=['create BaseModel', 'show BaseModel\
                           1234-1234-1234', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn('BaseModel', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        '''Test destroy command'''
        with patch('builtins.input',
                   side_effect=['create BaseModel', 'destroy\
                           BaseModel 1234-1234-1234', 'show BaseModel\
                           1234-1234-1234', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn('no instance found', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        '''Test all command'''
        with patch('builtins.input', side_effect=['all', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn('BaseModel', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        '''Test update command'''
        with patch('builtins.input',
                   side_effect=['create BaseModel', 'update\
                           BaseModel 1234-1234-1234 name "John"',
                                'show BaseModel 1234-1234-1234', 'quit']):
            HBNBCommand().cmdloop()
            output = mock_stdout.getvalue()
            self.assertIn('John', output)


if __name__ == '__main__':
    unittest.main()
