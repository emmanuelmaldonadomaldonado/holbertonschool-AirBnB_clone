#!/usr/bin/python3
"""
Unittest for Class Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    Test case
    """

    def place_attributes(self):
        """
        Test attribute initialization
        """
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
