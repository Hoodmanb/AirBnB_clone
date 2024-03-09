#!/usr/bin/python3
'''a file containing a class review that inherits from basemodel'''

from models.base_model import BaseModel


class Review(BaseModel):
    '''a review class that inherit from basemodel'''
    place_id = ""
    user_id = ""
    text = ""
