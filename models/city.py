#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city for the AirBnB clone project.

    Attributes:
        state_id (str): The state id of the city.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
