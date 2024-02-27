#!/usr/bin/python3
"""
Unittest for Class City
"""

import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """
    Test Case
    """

    def test_city_attributes(self):
        """
        Test Attribute Initialization
        """

        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
