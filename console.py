#!/usr/bin/python3
"""Create a class call HBNBCommmand"""


import cmd, shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Create the command interpreter"""
    prompt = '(hbnb) '

    """
    Classes dictionary to use with the commands
    """
    __classes_dict = {
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
        elif arg not in self.__classes_dict: # check if the argument is in the dictionary of classes
            print("** class doesn't exist **")
        else:
            new_instance = self.__classes_dict[arg]()
            new_instance.save()
            print(f"{new_instance.id}")

    def do_show(self, arg):
        """Display the instance"""
        arg = shlex.split(arg) # function to break it down into of individual arguments
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes_dict:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all() # get the dictionary from storage
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                print(f"{dict_from_storage[name_id]}")
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete the instance"""
        arg = shlex.split(arg) # function to break it down into of individual arguments
        if not arg:
            print("** class name missing **")
        elif arg[0] not in self.__classes_dict:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            dict_from_storage = storage.all()
            name_id = arg[0] + "." + arg[1]
            if name_id in dict_from_storage:
                del dict_from_storage[name_id]
            else:
                print("** no instance found **")
            storage.save()

    def do_all(self, arg):
        """print all dictionary"""
        list_obj = []
        if not arg:
            for obj in storage.all().values(): # get dictionary from th storage with the values
                list_obj.append(str(obj))
            print(list_obj)
        elif arg not in self.__classes_dict: # check if the argument is in the dictionary of classes
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if type(obj).__name__ == arg:
                    list_obj.append(str(obj))
            print(list_obj)

    def do_update(self, arg):
        """update <class name> <id> <attribute name> <attribute value>"""
        arg = shlex.split(arg)  # function to break it down into of individual arguments
        total_arguments = len(arg)
        argc_dict = {
            0: "** class name missing **",
            1: "** instance id missing **",
            2: "** attribute name missing **",
            3: "** value missing **"
            }

        if total_arguments in argc_dict:  # Prints error messages for argc_dict
            print(f"{argc_dict[total_arguments]}")
        else:
            if arg[0] not in self.__classes_dict:  # Check if class exists
                print("** class doesn't exist **")
            else:
                class_name = self.__classes_dict[arg[0]]
                dict_from_storage = storage.all()  # Get dict from storage
                name_id = arg[0] + "." + arg[1]
                attribute = arg[2]
                attribute_value = arg[3]

                if name_id in dict_from_storage:
                    obj = dict_from_storage[name_id]  # Get object

                    if hasattr(class_name, attribute):
                        attribute_type = type(getattr(class_name, attribute))
                        attribute_value = attribute_type(attribute_value)
                    setattr(obj, attribute, attribute_value)
                    obj.save()  # Save new update date and storage changes
                else:
                    print("** no instance found **")

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()