#!/usr/bin/python3
"""
    Defines the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
