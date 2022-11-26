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


class BaseModel:
    """ Parent class - Encharge of serialization/deserialization process
        Add an unique ID for every instace
        Add time for creating and updating
    """

    def __init__(self, *args, **kwargs):
        """
        Set inital values for every intance
        Args:
            *args: Is not used
            **kwargs: instance attributes - each key is an attribute name
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        val = datetime.strptime(value,
                                                '%Y-%m-%dT%H:%M:%S.%f')
                        setattr(self, key, val)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Represetation of a intaces
        Returns:
            str: [<class name>] (<self.id>) <self.__dict__>
        """
        cls = type(self).__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)

    def save(self):
        """
        Updates time and save changes into __objects (in FileStorage)
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        dictionary representation fo every intance
        time format: %Y-%m-%dT%H:%M:%S.%f
        key __class__ added to identify every intance
        Returns:
            dict: dictionary
        """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
