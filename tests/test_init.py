#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from storage.file_storage import FileStorage

class TestInitialization(unittest.TestCase):
    """Test cases for initialization of various classes."""

    def test_base_model_initialization(self):
        """Test initialization of BaseModel."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_user_initialization(self):
        """Test initialization of User."""
        user = User(username="test_user")
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, "test_user")
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.created_at, datetime)
        self.assertEqual(user.created_at, user.updated_at)

    def test_state_initialization(self):
        """Test initialization of State with name 'Nairobi'."""
        state = State(name="Nairobi")
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "Nairobi")
        self.assertIsInstance(state.id, str)
        self.assertIsInstance(state.created_at, datetime)
        self.assertEqual(state.created_at, state.updated_at)

    def test_file_storage_initialization(self):
        """Test initialization of FileStorage."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(storage._FileStorage__file_path, "file_storage.json")
        self.assertIsInstance(storage._FileStorage__objects, dict)

if __name__ == '__main__':
    unittest.main()

