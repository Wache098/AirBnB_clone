#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_reload(self):
        """Test the reload method."""
        # Create some objects
        state = State(name="California")
        user = User(username="test_user")
        state.save()
        user.save()

        # Reload objects from storage
        storage.reload()

        # Check if objects are reloaded correctly
        self.assertIn("{}.{}".format(State.__name__, state.id), storage.all())
        self.assertIn("{}.{}".format(User.__name__, user.id), storage.all())


if __name__ == "__main__":
    unittest.main()
