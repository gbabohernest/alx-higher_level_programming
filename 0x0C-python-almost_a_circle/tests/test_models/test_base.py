#!usr/bin/python3
import unittest
from models.base import Base

"""This module defines test cases for the base module"""


class TestBase(unittest.TestCase):
    """Defines test cases for Base class"""

    def test_no_id(self):
        """Test no id provided"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_no_id_twice(self):
        """Test no id provided twice"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_with_id(self):
        """Test with id provided"""
        b3 = Base(22)
        self.assertEqual(b3.id, 22)

    def test_id_with_negative(self):
        """Test with negative number"""
        b4 = Base(-50)
        self.assertEqual(b4.id, -50)

    def test_id_with_zero(self):
        """Test with id == 0"""
        b5 = Base(0)
        self.assertEqual(b5.id, 0)

    # Test id as non integer value
    def test_id_with_string(self):
        """Test with id as a string"""
        b6 = Base("string")
        self.assertEqual(b6.id, "string")

    def test_id_with_list(self):
        """Test with id as a list"""
        value = [1, 3, 'hi', 'there']
        b7 = Base(value)
        self.assertEqual(b7.id, value)

    def test_id_with_dict(self):
        """Test with id as a dictionary"""
        id_dict = {"name": "John Doe", "age": 130}
        b8 = Base(id_dict)
        self.assertEqual(b8.id, id_dict)

    def test_id_with_tuple(self):
        """Test with id as a tuple"""
        id_tuple = (2, 3)
        b9 = Base(id_tuple)
        self.assertEqual(b9.id, id_tuple)

    def test_cls_private_attribute(self):
        b10 = Base(10)
        with self.assertRaises(AttributeError):
            print(b10.id.__nb_instances)
