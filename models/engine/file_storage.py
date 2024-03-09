#!/usr/bin/python3

'''a file containing a class that serializes instances
to a JSON file and deserializes JSON file to instances'''
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''-_file_path (str): The name of the file to save objects     to.
    -__objects (dict): A dictionary of instantiated objects'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        objName = obj.__class__.__name__
        FileStorage.__objects[f"{objName}.{obj.id}"] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        serializable_objects = {k: v.to_dict(
            ) for k, v in self.__class__.__objects.items(
            ) if not isinstance(v, FileStorage)}
        with open(self.__class__.__file_path, "w") as f:
            json.dump(serializable_objects, f, default=lambda o: o.__dict__)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
