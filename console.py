#!/usr/bin/python3
'''contains the contains the entry point of the command interpreter'''

import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''class defimition for my command line interpreter'''
    valid_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
                     'Place', 'Review']

    prompt = "(hbnb) "

    def do_quit(self, arg):
        '''this quit or exit the program'''
        return True

    do_EOF = do_quit

    def do_create(self, arg):
        '''creates a new instance of a class passed as an argument'''
        """Create command to create a new instance of BaseModel,
        save it in a JSON file and prints the id.
        Attributes:args (str): inputted line in command prompt.
        """
        line = arg.split()
        if not self.verify_class(line):
            return
        instance = eval(line[0] + '()')
        if isinstance(instance, BaseModel):
            instance.save()
            print(instance.id)
        return

    def do_show(self, arg):
        '''Prints the string representation of an instance based
        on the class name and id'''
        line = arg.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        print(objects[key])

    def do_destroy(self, args):
        """Destroy command that deletes an instance based on the class name
        and id. Save the change in JSON file.
        Attributes:
            args (str): inputted line in command prompt.
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        key = '{}.{}'.format(line[0], line[1])
        objects = models.storage.all()
        del objects[key]
        models.storage.save()

    def do_all(self, args):
        """
        Prints all string representation of all instances based
        or not on the class name.
        """
        line = args.split()
        objects = models.storage.all()
        to_print = []
        if len(line) == 0:
            for v in objects.values():
                to_print.append(str(v))
        elif line[0] in HBNBCommand.valid_classes:
            for k, v in objects.items():
                if line[0] in k:
                    to_print.append(str(v))
        else:
            print("** class doesn't exist **")
            return False
        print(to_print)

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        """
        line = args.split()
        if not self.verify_class(line):
            return
        if not self.verify_id(line):
            return
        if not self.verify_attribute(line):
            return
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        setattr(objects[key], line[2], line[3])
        models.storage.save()

    @classmethod
    def verify_class(cls, line):
        """Static method to verify inputed class"""
        if len(line) == 0:
            print('** class name missing **')
            return False
        elif line[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
            return False
        return True

    @staticmethod
    def verify_id(line):
        """Static method to ferify the id.
        """
        if len(line) < 2:
            print('** instance id missing **')
            return False
        objects = models.storage.all()
        key = '{}.{}'.format(line[0], line[1])
        if key not in objects.keys():
            print('** no instance found **')
            return False
        return True

    @staticmethod
    def verify_attribute(line):
        """Static method to verify the attribute in inputted line.
        """
        if len(line) < 3:
            print("** attribute name missing **")
            return False
        elif len(line) < 4:
            print("** value missing **")
            return False
        return True

    def emptyline(self):
        "print the prompt on a new line when enter is clicked without an arg"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
