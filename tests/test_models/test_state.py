#!/usr/bin/python3
"""
Unittest for Class State
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    Test Case
    """

    def test_state_attributes(self):
        """
        Test attribute initialization
        """
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
