#!/usr/bin/python3

import unittest
from models.state import State

class TestState(unittest.TestCase):
     """Test cases for the State class."""

    def test_init(self):
        """Test the initialization of the State class."""
        state = State(name="Nairobi")
        self.assertEqual(state.name, "Nairobi")

if __name__ == '__main__':
    unittest.main()
