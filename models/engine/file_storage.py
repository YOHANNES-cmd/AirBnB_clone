#!/usr/bin/python3
""" Engine package for the AirBnB """
import json
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    """
    FileStorage class - store the objects
    Class Attributes:
        __file_path (str): path of the JSON file where data is stored
        __objects (dict): dictionary where the instances are stored
        name_classes (dict): dictionary where the different kind of classes are
                             stored
    """

    __file_path = "file.json"
    __objects = {}
    name_classes = {"BaseModel": BaseModel, "User": User,
                    "Place": Place, "State": State, "City": City,
                    "Amenity": Amenity, "Review": Review}

    def all(self):
        """
        all - return the dictionary where the instances are stored
        Args:
            None
        Returns:
            the dictionary where the instancces are stored
        """
        return self.__objects

    def new(self, obj):
        """
        new - saves a new instance
        Args:
            obj (class instance): object to be stored
        Returns:
            None
        """
        cls = type(obj).__name__
        FileStorage.__objects.update({'{}.{}'.format(cls, obj.id): obj})

    def save(self):
        """
        save - save objects to JSON file
        Args:
            None
        Returns:
            None
        """
        with open(FileStorage.__file_path, mode="w") as file:
            aux_dict = {}
            for key, obj in FileStorage.__objects.items():
                aux_dict.update({key: obj.to_dict()})
            file.write(json.dumps(aux_dict))

    def reload(self):
        """
        reload - loads from JSON file
        Args:
            None
        Returns:
            None
        """
        try:
            with open(FileStorage.__file_path) as file:
                aux_dict = json.loads(file.read())
            for key, obj in sorted(aux_dict.items()):
                model = key.split(".")[0]
                modelval = FileStorage.name_classes.get(model)
                aux_dict.update({key: modelval(**obj)})
            FileStorage.__objects = aux_dict
        except FileNotFoundError:
            pass

    def delete(self, class_name, ids):
        """
        delete - delete an instance from the storage
        Args:
            class_name (str): name of the class
            ids (str): id of the instance
        Returns:
            None
        """
        aux = "{}.{}".format(class_name, ids)
        FileStorage.__objects.pop(aux)
        self.save()
