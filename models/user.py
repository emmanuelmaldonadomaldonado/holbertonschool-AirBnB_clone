#!/usr/bin/python3
"""
Class User inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class has public attributes and updates
    FileStorage to manage serialization and
    deserialization of User
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
