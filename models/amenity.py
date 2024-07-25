#!/usr/bin/python3
"""Unittests for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_str(self):
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)


if __name__ == "__main__":
    unittest.main()
