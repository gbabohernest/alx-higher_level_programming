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


class TestToJsonString(unittest.TestCase):
    """Defines test cases for the static method to_json_string"""
    def setUp(self):
        """Set up each test cases for to_json_string method"""
        self.sq = Square(4, 3, 2, 1)
        self.sq2 = Square(10, 20, 30, 40)
        self.rect = Rectangle(4, 3, 3, 1, 2)
        self.rect2 = Rectangle(50, 60, 70, 80, 90)
        self.dictionary = self.sq.to_dictionary()
        self.dict2 = self.sq2.to_dictionary()
        self.rect_dict = self.rect.to_dictionary()
        self.rect_dict2 = self.rect2.to_dictionary()

    def tearDown(self):
        """Run clean up after each test cases for to_json_string method"""
        del self.sq
        del self.sq2
        del self.rect
        del self.rect2
        del self.dictionary
        del self.dict2
        del self.rect_dict
        del self.rect_dict2

    def test_to_json_string_no_args(self):
        """Test for no args"""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_args(self):
        """Test for more args"""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)

    def test_to_json_string_type(self):
        """Testing the type the method will return
        when use with the type function"""
        json_string = Base.to_json_string([self.dictionary])
        self.assertEqual(type(json_string), str)
        self.assertEqual(type(Base.to_json_string([self.rect_dict])), str)

    def test_to_json_string_None(self):
        """Testing for when None is passed in as arg"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_value(self):
        """Testing for correct output value"""
        json_string = Base.to_json_string([self.dictionary])
        data = json.loads(json_string)
        self.assertEqual(data, [{'id': 1, 'x': 3, 'size': 4, 'y': 2}])

    def test_to_json_string_empty(self):
        """Testing for empty json string"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_dict_len(self):
        """Test length of one dict as input"""
        json_string = Base.to_json_string([self.dictionary])
        self.assertTrue(len(json_string) == 38)
        self.assertTrue(len(Base.to_json_string([self.rect_dict])) == 52)

    def test_to_json_string_len_with_two_dict(self):
        """Test length of two dict as input"""
        json_string = Base.to_json_string([self.dictionary, self.dict2])
        self.assertTrue(len(json_string) == 80)

        rect_string = Base.to_json_string([self.rect_dict, self.rect_dict2])
        self.assertTrue(len(rect_string) == 109)
