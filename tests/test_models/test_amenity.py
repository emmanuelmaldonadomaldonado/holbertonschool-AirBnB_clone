#!/usr/bin/python3
"""
Unittest for Class Amenity
"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test case
    """

    def test_amenity_attributes(self):
        """
        Attribute initialization
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
