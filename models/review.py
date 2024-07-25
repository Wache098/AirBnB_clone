#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review for the AirBnB clone project.

    Attributes:
        place_id (str): The Place.id linked to the review.
        user_id (str): The User.id linked to the review.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
