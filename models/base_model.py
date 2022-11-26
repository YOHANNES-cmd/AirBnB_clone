#!/usr/bin/python3
"""
    Class BaseModel that defines all common attributes
    and methods for other classes
"""
import models
import json
import uuid
from uuid import uuid4
from datetime import datetime

dform = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The AirBnB Base Model"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, dform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """str() representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["__class__"] = self.__class__.__name__
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        return rdict
