#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

from models import storage
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class for all other classes to inherit from.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance
        """

        time = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], time)
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
            storage.save()

    def save(self):
        """
        Saves the instance to the storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """
        Returns a string representation of the instance.
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = type(self).__name__
        return obj_dict
