#!/usr/bin/python3

from .base_model import BaseModel


class User(BaseModel):
    """
    User class for AirBnB objects, inheriting from BaseModel.

    Attributes:
        username (str): The username of the user.
    """

    def __init__(self, username):
        """
        Initializes a new User instance.

        Args:
            username (str): The username of the user.
        """
        super().__init__()
        self.username = username
