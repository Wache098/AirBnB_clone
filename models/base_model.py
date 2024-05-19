#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    """
    Base class for all models.

    Attributes:
        id (str): The unique identifier for the instance.
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the instance was last updated.
    """

    def __init__(self, **kwargs):
        """
        Initialize a new BaseModel instance.

        Args:
            **kwargs: Arbitrary keyword arguments to set instance attributes.
        """
        self.id = str(uuid.uuid4())  # Generate unique ID
        self.created_at = datetime.now()  # Set created_at to current datetime
        self.updated_at = self.created_at  # Set updated_at to created_at initially
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: String representation of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update updated_at with current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary containing all keys/values of the instance.

        Returns:
            dict: Dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
