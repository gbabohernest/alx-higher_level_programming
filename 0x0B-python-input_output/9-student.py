#!/usr/bin/python3
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

    def to_json(self):
        """Retrieves a dictionary
        representation of an instance
        """
        return self.__dict__
