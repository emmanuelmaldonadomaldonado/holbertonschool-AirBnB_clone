#!/usr/bin/python3
""" Unit test module for BaseModel class """

import unittest
import os
from models.engine.file_storage import FileStorage
from datetime import datetime
from models.base_model import BaseModel


my_model = BaseModel()


class TestBase(unittest.TestCase):
    """ Class for BaseModel tests """

    def test_id(self):
        """ Unittesting test_id instance """
        self.assertTrue(type(my_model.id) is str)

    def test_created_at(self):
        """ Unittesting created_at instance """
        self.assertTrue(type(my_model.created_at) is datetime)

    def test_str(self):
        """ Unittesting __str__ method """
        expected = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(expected, str(my_model))

    def test_to_dict(self):
        """ Unittesting to_dict method """
        my_dict = my_model.to_dict()
        self.assertTrue(type(my_dict["created_at"]) is str)
        self.assertTrue(type(my_dict) is dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertIn("__class__", my_dict.keys())

    def test_save(self):
        """ Unittesting save method """
        my_save = my_model.updated_at
        my_model.save()
        self.assertTrue(os.path.exists("file.json"))
        my_save2 = my_model.updated_at
        self.assertNotEqual(my_save, my_save2)


if __name__ == '__main__':
    unittest.main()
