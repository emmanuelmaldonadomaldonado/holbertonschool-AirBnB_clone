#!/usr/bin/python3
"""
Class State inherits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class has public attributes and updates
    FileStorage to manage serialization and
    deserialization
    """

    name = ""
