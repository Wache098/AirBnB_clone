#!/usr/bin/python3
from .base_model import BaseModel


class State(BaseModel):
    """
    State class for AirBnB objects, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, **kwargs):
        """Initialize a new State instance."""
        super().__init__(**kwargs)
