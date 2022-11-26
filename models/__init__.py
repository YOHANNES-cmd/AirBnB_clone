#!/usr/bin/python3
"""__init__ magic method for models directory"""
import models
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


storage = FileStorage()
storage.reload()
