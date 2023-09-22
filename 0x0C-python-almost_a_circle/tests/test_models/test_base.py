#!usr/bin/python3
import os
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


class TestBase_save_to_file(unittest.TestCase):
    """Tests for the class method save_to_file"""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_save_to_file_into_json(self):
        """Test saving into json format"""
        rect = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        list_dict = [{"x": 0, "y": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(list_dict, json.loads(content))

    def test_save_to_file_one_rectangle(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])

        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])

        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)

    def test_save_to_file_one_square(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])

        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_None(self):
        """Testing saving a file into
            json format sending None
        """
        rect = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual("[]", content)

    def test_save_to_file_two_squares(self):
        sq1 = Square(10, 7, 2, 8)
        sq2 = Square(8, 1, 2, 3)
        Square.save_to_file([sq1, sq2])

        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        sq = Square(10, 7, 2, 8)
        Base.save_to_file([sq])

        with open("Base.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_overwrite(self):
        sq = Square(9, 2, 39, 2)
        Square.save_to_file([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])

        with open("Square.json", "r") as file:
            self.assertTrue(len(file.read()) == 39)

    def test_save_to_file_None_sq(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)

    def test_save_to_file_type(self):
        """Testing saving a file into
           json format sending None
        """
        rect = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass


class TestBase_save_to_file_csv(unittest.TestCase):
    """Defines test for the method save_to_file_cvs"""

    def tearDown(self):
        """Delete created file after each test case"""
        try:
            os.remove("Base.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as fd:
            self.assertEqual("", fd.read())

    def test_save_to_file_csv_overwrite(self):
        """Test saving a square instance which
        over-writes another sq instance
        """
        sq = Square(9, 2, 39, 2)
        Square.save_to_file_csv([sq])
        sq = Square(10, 7, 2, 8)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as fd:
            self.assertTrue("8,10,7,2", fd.read())

    def test_save_to_file_csv_square_one(self):
        """Test saving a square instance as csv file"""
        sq = Square(30, 17, 22, 18)
        Square.save_to_file_csv([sq])
        with open("Square.csv", "r") as fd:
            self.assertTrue("18,30,17,22", fd.read())

    def test_save_to_file_csv_squares_two(self):
        """Test saving two square instances as csv file"""
        sq1 = Square(30, 17, 22, 18)
        sq2 = Square(18, 1, 12, 23)
        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as fd:
            self.assertTrue("18,30,17,22\n23,18,11,12", fd.read())

    def test_save_to_file_csv_rectangle_one(self):
        rect = Rectangle(5, 17, 2, 8, 15)
        Rectangle.save_to_file_csv([rect])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("15,5,17,2,8", fd.read())

    def test_save_to_file_csv_rectangles_two(self):
        rect1 = Rectangle(5, 17, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as fd:
            self.assertTrue("15,5,17,2,8\n2,4,1,2,3", fd.read())


class TestBase_create(unittest.TestCase):
    """Test cases for testing  the class
        method create  of Base class.
        """

    def test_create_square_equals(self):
        """Test equal square"""
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)

    def test_create_square_original(self):
        """Test original square with the dict output"""
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq1))

    def test_create_square_new(self):
        """Test new square with the create method output"""
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (7) 5/1 - 3", str(sq2))

    def test_create_square_is(self):
        """Test if sq1 & sq2 """
        sq1 = Square(3, 5, 1, 7)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_create_rectangle_original(self):
        """Test original rectangle with the original output"""
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect1))

    def test_create_rectangle_new(self):
        """Test the create method output"""
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(rect2))

    def test_create_rectangle_is(self):
        """Test if rect1 and rect2"""
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equals(self):
        """Test for equality"""
        rect1 = Rectangle(3, 5, 1, 2, 7)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)


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


class TestBase_load_from_file(unittest.TestCase):
    """Defines test cases for the class method load_from_a_file"""

    @classmethod
    def tearDown(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_same_y(self):
        """Test that an object was created from the
           list and has the same y
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect_input_list = [rect1]

        Rectangle.save_to_file(rect_input_list)
        rect_input_list = Rectangle.load_from_file()
        self.assertEqual(rect1.y, rect_input_list[0].y)

    def test_load_from_file_same_height(self):
        """Test that an object was created from the
            list and has the same height
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect_input_list = [rect1]

        Rectangle.save_to_file(rect_input_list)
        rect_input_list = Rectangle.load_from_file()
        self.assertEqual(rect1.height, rect_input_list[0].height)

    def test_load_from_file_first_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        sq_output_list = Square.load_from_file()
        self.assertEqual(str(sq1), str(sq_output_list[0]))

    def test_load_from_file_second_square(self):
        sq1 = Square(5, 1, 3, 3)
        sq2 = Square(9, 5, 2, 3)
        Square.save_to_file([sq1, sq2])
        sq_output_list = Square.load_from_file()
        self.assertEqual(str(sq2), str(sq_output_list[1]))

    def test_load_from_file_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)

    def test_load_from_file_not_the_same(self):
        """Test that an object was created from the
            list but has a different address.
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect_input_list = [rect1]

        Rectangle.save_to_file(rect_input_list)
        rect_input_list = Rectangle.load_from_file()
        self.assertNotEqual(id(rect1), id(rect_input_list[0]))

    def test_load_from_file_square_types(self):
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_same_width(self):
        """Test that an object was created from the
            list and has the same width
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect_input_list = [rect1]

        Rectangle.save_to_file(rect_input_list)
        rect_input_list = Rectangle.load_from_file()
        self.assertEqual(rect1.width, rect_input_list[0].width)

    def test_load_from_file_same_x(self):
        """Test that an object was created from the
            list and has the same x
        """
        rect1 = Rectangle(10, 7, 2, 8)
        rect_input_list = [rect1]

        Rectangle.save_to_file(rect_input_list)
        rect_input_list = Rectangle.load_from_file()
        self.assertEqual(rect1.x, rect_input_list[0].x)

    def test_load_from_file_first_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        rect_output_list = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(rect_output_list[0]))

    def test_load_from_file_second_rectangle(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        rect_output_list = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(rect_output_list[1]))

    def test_load_from_file_rectangle_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([rect1, rect2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))


class TestBase_load_from_file_csv(unittest.TestCase):
    """Defines tests for load_from_file method"""

    def tearDown(self):
        """Delete created files after each test case"""

        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_load_from_file_csv_more_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)

    def test_load_from_file_csv_empty_file_arg(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_from_file_csv_sq_types(self):
        sq1 = Square(25, 11, 23, 33)
        sq2 = Square(19, 15, 12, 13)
        Square.save_to_file_csv([sq1, sq2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))

    def test_load_from_file_csv_rect_types(self):
        rect1 = Rectangle(11, 17, 12, 18, 11)
        rect2 = Rectangle(22, 24, 25, 26, 22)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_sq_index(self):
        sq1 = Square(25, 11, 23, 33)
        sq2 = Square(19, 15, 12, 13)
        Square.save_to_file_csv([sq1, sq2])
        sq_output = Square.load_from_file_csv()
        self.assertEqual(sq1.__str__(), str(sq_output[0]))

    def test_load_from_file_csv__first_rect_index(self):
        rect1 = Rectangle(11, 17, 12, 18, 11)
        rect2 = Rectangle(22, 24, 25, 26, 22)
        Rectangle.save_to_file_csv([rect1, rect2])
        rect_output = Rectangle.load_from_file_csv()
        self.assertEqual(rect1.__str__(), str(rect_output[0]))

    def test_load_from_file_csv_multiple_square(self):
        sq1 = Square(25, 11, 23, 33)
        sq2 = Square(19, 15, 12, 13)
        Square.save_to_file_csv([sq1, sq2])
        sq_output = Square.load_from_file_csv()
        self.assertEqual(sq2.__str__(), str(sq_output[1]))

    def test_load_from_file_csv__second_rect_index(self):
        rect1 = Rectangle(11, 17, 12, 18, 11)
        rect2 = Rectangle(22, 24, 25, 26, 22)
        Rectangle.save_to_file_csv([rect1, rect2])
        rect_output = Rectangle.load_from_file_csv()
        self.assertEqual(rect2.__str__(), str(rect_output[1]))
