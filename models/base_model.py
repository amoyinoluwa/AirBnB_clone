#!/usr/bin/python3
""" Module base_model
Contains BaseModel class
"""

import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """ Represent a class BaseModel that defines
    all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if (key != '__class__'):
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            """Initializes the unique id for each BaseModel"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints model"""
        class_name = self.__class__.__name__
        res  = "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
        return res

    def save(self):
        """
        updates the public instance attribute `updated_at with
        the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance"""
        class_dict = dict()
        dates = set(["created_at", "updated_at"])
        for key, value in self.__dict__.items():
            if key in dates:
                class_dict[key] = value.isoformat()
            else:
                class_dict[key] = value
        class_dict["__class__"] = self.__class__.__name__
        return class_dict
