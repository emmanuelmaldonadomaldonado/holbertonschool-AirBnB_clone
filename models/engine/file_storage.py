#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objects, f)
    
    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State

        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        cls = BaseModel
                    elif class_name == "User":
                        cls = User
                    elif class_name == "Amenity":
                        cls = Amenity
                    elif class_name == "City":
                        cls = City
                    elif class_name == "Place":
                        cls = Place
                    elif class_name == "Review":
                        cls = Review
                    elif class_name == "State":
                        cls = State
                    else:
                        continue
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
