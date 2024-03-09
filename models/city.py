#!/usr/bin/python3
'''a file containing a class city that inherits from b    asemodel'''

from models.base_model import BaseModel


class City(BaseModel):
    '''a city class that inherit from basemodel'''
    state_id = ""
    name = ""
