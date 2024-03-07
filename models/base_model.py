#!/usr/bin/python3

'''base class that defines all common attributes/methods for other classes'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''Class for base model of object hierarchy.'''

    def __init__(self, *args, **kwargs):
        '''initialisation of basemodel args
        -*args = list of arguments
        -**kwargs = dictionary of keyvalue argument
        -id
        -created_at
        -updated_at'''

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__['created_at'] = datetime.strptime(
                            kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__['updated_at'] = datetime.strptime(
                            kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''string representation of the baseclass'''

        return f"{[type(self).__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        '''updates the public instance attribute
        updated_at with the current datetime'''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''returns a dictionary containing all
        keys/values of __dict__ of the instance'''

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = obj_dict['created_at'].isoformat()
        obj_dict['updated_at'] = obj_dict['updated_at'].isoformat()
        return obj_dict
