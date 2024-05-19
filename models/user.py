#!/usr/bin/python3

from .base_model import BaseModel


class User(BaseModel):
    """
    User class for AirBnB objects, inheriting from BaseModel.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new User instance.
        """
        super().__init__(**kwargs)
