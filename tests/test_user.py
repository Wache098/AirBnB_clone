#!/usr/bin/python3

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_init(self):
        """Test the initialization of the User class."""
        user = User(username="test_user")
        self.assertEqual(user.username, "test_user")

if __name__ == '__main__':
    unittest.main()
