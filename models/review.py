#!/usr/bin/python3
"""
Class Review inherits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class has public attributes and updates
    FileStorage to manage serialization and
    deserialization
    """
    
    place_id = ""
    user_id = ""
    text = ""
