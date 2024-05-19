#!/usr/bin/python3

import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State


class FileStorage:
    """FileStorage class for AirBnB clone project."""

    def __init__(self):
        """Initialize a new FileStorage instance."""
        self.__file_path = "file_storage.json"
        self.__objects = {}

    def all(self):
        """Return the dictionary of all objects."""
        return self.__objects

    def new(self, obj):
        """Add a new object to storage."""
        self.__objects[obj.id] = obj

    def save(self):
        """Save all objects to file."""
        with open(self.__file_path, 'w') as f:
            json.dump({obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}, f)

    def reload(self):
        """Reload objects from file."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for obj_id, obj_data in data.items():
                    class_name = obj_data['__class__']
                    if class_name == 'BaseModel':
                        self.__objects[obj_id] = BaseModel(**obj_data)
                    elif class_name == 'User':
                        self.__objects[obj_id] = User(**obj_data)
                    elif class_name == 'State':
                        self.__objects[obj_id] = State(**obj_data)
