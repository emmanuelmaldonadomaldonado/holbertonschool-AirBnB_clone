#!/usr/bin/python3
"""
Class Amenity inherits from BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class has public attributes and updates
    FileStorage to manage serialization and
    deserialization
    """
    
    name = ""
