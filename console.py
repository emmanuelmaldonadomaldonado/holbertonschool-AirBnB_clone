#!/usr/bin/python3
"""Create a class called HBNBCommand"""

import cmd
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Create the command interpreter"""
    prompt = '(hbnb) '
    classes_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (CRTL - d)"""
        print("Exiting the program")
        return True

    def cmdloop(self):
        """so that th console stays in a loop"""
        try:
            super().cmdloop()
        except KeyboardInterrupt:
            return True

    def do_create(self, arg):
        """Create a new instance with the dictionary of classes"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes_dict:
            print("** class doesn't exist **")
            return
        new_instance = self.classes_dict[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Display the instance"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in self.classes_dict:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Delete the instance"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in self.classes_dict:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        elif arg in self.classes_dict:
            print([str(obj) for obj in objects.values()
                   if isinstance(obj, self.classes_dict[arg])])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance"""
        args = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        if args[0] not in self.classes_dict:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        setattr(objects[key], args[2], args[3])
        storage.save()

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
