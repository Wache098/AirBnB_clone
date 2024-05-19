#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def test_instance_creation(self):
        """Test that a new BaseModel instance is correctly created."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_str_method(self):
        """Test the __str__ method of BaseModel."""
        model = BaseModel()
        string_representation = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), string_representation)

    def test_save_method(self):
        """Test the save method of BaseModel."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())

if __name__ == "__main__":
    unittest.main()

