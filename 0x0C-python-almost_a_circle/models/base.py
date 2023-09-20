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
        # if list_dictionaries is None or list_dictionaries == []:
        #     return "[]"
        # return json.dumps(list_dictionaries)

        if list_dictionaries is None:
            return "[]"

        if not isinstance(list_dictionaries, list):
            raise TypeError("must be a list")

        if not all(isinstance(item, dict) for item in list_dictionaries):
            raise TypeError("must be a list of dictionaries")

        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @staticmethod
    def from_json_string(json_string):
        """Return a list of JSON string representation.

        arg:
            json_string: a string representation of
                        a list of dictionaries
        """
        if json_string is None:
            return []

        if type(json_string) != str:
            raise TypeError("must be a string")

        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a JSON string representation
        of list_objs to a file.

        args:
            list_objs: list of instances who inherits from Base.
            Example (list of Rectangle, or list of Square) instances.
        """

        file_name = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for idx, item in enumerate(list_objs):
                item = item.to_dictionary()
                dictionary = json.loads(cls.to_json_string(item))
                content.append(dictionary)

        with open(file_name, mode="w") as file_pointer:
            json.dump(content, file_pointer)
