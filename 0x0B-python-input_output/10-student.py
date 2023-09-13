"""This module defines a Student Class"""


class Student:
    """Defines a student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiate with three instance variables
        args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary
        representation of an instance
        """
        filtered_dict = {}

        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

        return {}
