#!usr/bin/python3
import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

"""This module defines test cases for the base module"""


class TestBase_init(unittest.TestCase):
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


class TestBase_to_json_string(unittest.TestCase):
    """Defines test cases for the static method to_json_string"""

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
        sq = Square(4, 3, 2, 1)
        dictionary = sq.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        self.assertEqual(type(json_string), str)

        rect = Rectangle(4, 3, 3, 1, 2)
        rect_dict = rect.to_dictionary()
        json_string = Base.to_json_string([rect_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_string_None(self):
        """Testing for when None is passed in as arg"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_rectangle_value(self):
        """Testing for correct output value"""
        rect = Rectangle(10, 7, 2, 8, 1)
        dictionary = rect.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        data = json.loads(json_string)
        self.assertEqual(data, [{'x': 2, 'width': 10, 'id': 1,
                                'height': 7, 'y': 8}])

    def test_to_json_string_value(self):
        """Testing for correct output value"""
        sq = Square(4, 3, 2, 1)
        dictionary = sq.to_dictionary()
        json_string = Base.to_json_string([dictionary])
        data = json.loads(json_string)
        self.assertEqual(data, [{'id': 1, 'x': 3, 'size': 4, 'y': 2}])

    def test_to_json_string_empty_list(self):
        """Testing for empty json string"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_dict_len(self):
        """Test length of one dict as input"""
        sq = Square(4, 3, 2, 1)
        sq_dict = sq.to_dictionary()
        json_string = Base.to_json_string([sq_dict])
        self.assertTrue(len(json_string) == 38)

        rect = Rectangle(4, 3, 3, 1, 2)
        rect_dict = rect.to_dictionary()
        json_string = Base.to_json_string([rect_dict])
        self.assertTrue(len(json_string) == 52)

    def test_to_json_square_len_with_two_dict(self):
        """Test length of two square dict as input"""
        sq = Square(4, 3, 2, 1)
        sq2 = Square(10, 20, 30, 40)
        sq_dict = [sq.to_dictionary(), sq2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(sq_dict)) == 80)

    def test_to_json_rectangle_len_with_two_dict(self):
        """Test length of two rectangle dict as input"""
        rect = Rectangle(4, 3, 3, 1, 2)
        rect2 = Rectangle(50, 60, 70, 80, 90)
        rect_dict = [rect.to_dictionary(), rect2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(rect_dict)) == 109)


class TestBase_from_json_string(unittest.TestCase):
    """Defines test cases for the method from_json_string"""

    def test_from_json_string_return_type(self):
        """check method return type"""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_success(self):
        """Testing that the json string gets converted into a list"""
        list_input = [
            {'id': 2089, 'width': 10, 'height': 4},
            {'id': 2712, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        s1 = {'id': 2089, 'width': 10, 'height': 4}
        s2 = {'height': 7, 'id': 2712, 'width': 1}
        self.assertEqual(list_input[0], s1)
        self.assertEqual(list_input[1], s2)

    def test_from_json_string_one_rect(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_type(self):
        """Testing the returned type of the method"""
        list_input = [
            {'id': 2089, 'width': 10, 'height': 4},
            {'id': 2712, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)

    def test_from_json_string_two_rect(self):
        """Test if two rectangle are equal"""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_sq(self):
        """Test square if its equal to what the method return"""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_sq(self):
        """Test for comparing two squares """
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        """check for none"""
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        """Test for empty list"""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        """Test no arg error"""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        """check for more than one args error"""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)
