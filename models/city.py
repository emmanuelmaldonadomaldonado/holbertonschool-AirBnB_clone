#!/usr/bin/python3
"""
Class City inherits from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class has public attributes and updates
    FileStorage to manage serialization and
    deserialization
    """

    state_id = ""
    name = ""
