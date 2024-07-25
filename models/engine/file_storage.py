#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State

class FileStorage:
    """
    File storage engine for AirBnB objects.

    Attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): Dictionary of stored objects.
    """

    def __init__(self):
        """
        Initializes a new FileStorage instance.
        """
        self.__file_path = "file_storage.json"
        self.__objects = {}

    def all(self):
        """
        Returns the dictionary of stored objects.

        Returns:
            dict: Dictionary of stored objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the storage.

        Args:
            obj: The object to add.
        """
        self.__objects[obj.id] = obj

    def save(self):
        """
        Saves the objects to the JSON file.
        """
        with open(self.__file_path, 'w') as f:
            json.dump({obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}, f)

    def reload(self):
        """
        Loads objects from the JSON file.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for obj_id, obj_data in data.items():
                    class_name = obj_data['__class__']
                    self.__objects[obj_id] = globals()[class_name].from_dict(obj_data)
