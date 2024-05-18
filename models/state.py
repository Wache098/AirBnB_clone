#!/usr/bin/python3
from .base_model import BaseModel


class State(BaseModel):
    """
    State class for AirBnB objects, inheriting from BaseModel.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, name):
        """
        Initializes a new State instance.

        Args:
            name (str): The name of the state.
        """
        super().__init__()
        self.name = name

