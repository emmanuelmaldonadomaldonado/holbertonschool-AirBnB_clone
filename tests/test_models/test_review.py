#!/usr/bin/python3
"""
Unittest for Class Review
"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """
    Test Case
    """

    def test_review_attributes(self):
        """
        Test Attribute Initialization
        """
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()
