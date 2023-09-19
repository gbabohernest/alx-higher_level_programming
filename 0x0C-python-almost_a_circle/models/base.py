#!/usr/bin/python3
"""The module defines a Base class for all other classes.
Its goal is to manage id attribute in all future classes.
"""
import json


class Base:
    """Base class.
    This class will be the "base" of all other classes in this project.
    It will manage id attribute for all the classes

    args:
         @id: The id for a specific instance.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a new Base.

        arg:
            @id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
