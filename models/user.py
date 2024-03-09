#!/usr/bin/python3
'''a file containing a class User that inherits from BaseModel'''

from models.base_model import BaseModel


class User(BaseModel):
    '''class representing a user'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
