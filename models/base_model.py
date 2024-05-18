#!/usr/bin/python3

import uuid
from datetime import datetime


class BaseModel:
     """
    Base class for AirBnB objects.

    Attributes:
        id (str): Unique identifier for the object.
        created_at (datetime): Timestamp of when the object was created.
        updated_at (datetime): Timestamp of when the object was last updated.
    """


    def __init__(self):
         """
        Initializes a new instance of the BaseModel class.

        Sets id to a unique identifier, created_at and updated_at to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
         """
        Returns a string representation of the object.

        Returns:
            str: String representation of the object.
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
         """
        Converts the object to a dictionary representation.

        Returns:
            dict: Dictionary representation of the object.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
