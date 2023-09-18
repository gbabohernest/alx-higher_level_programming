#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle

"""This module defines test cases for the rectangle module"""


class TestRectangle(unittest.TestCase):
    """Test cases for rectangle instance"""

    # Test Rectangle for empty, less, more args
    def test_rect_isinstance(self):
        """check if Rectangle inherits from base"""
        rect = Rectangle(20, 10)
        self.assertIsInstance(rect, Base)

    def test_no_args(self):
        """instance with no args"""
        with self.assertRaises(TypeError):
            rect = Rectangle()

    def test_with_arg(self):
        """instance with one arg"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2)

    def test_with_excess_args(self):
        """Test with more args then required"""
        with self.assertRaises(TypeError):
            rect = Rectangle(20, 10, 2, 3, 22, 44)

    # Test Rectangle Instance Attribute (Getter & Setter Methods)
    def test_rect_width_attr(self):
        """Test instance width attribute"""
        rect = Rectangle(20, 10)
        self.assertEqual(rect.width, 20)

    def test_rect_width_setter(self):
        """Test width setter method"""
        rect = Rectangle(20, 10)
        rect.width = 22
        self.assertEqual(rect.width, 22)

    def test_rect_height_attr(self):
        """Test instance height attr"""
        rect = Rectangle(20, 10)
        self.assertEqual(rect.height, 10)

    def test_rect_height_setter(self):
        """Test height setter method"""
        rect = Rectangle(20, 10)
        rect.height = 20
        self.assertEqual(rect.height, 20)

    def test_rect_x_attr(self):
        """Test instance x attribute"""
        rect = Rectangle(20, 10, x=3)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 0)

    def test_rect_x_setter(self):
        """Test x setter method"""
        rect = Rectangle(1, 1, 2, 0, 5)
        rect.x = 10
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 0)

    def test_rect_y_attr(self):
        """Test instance y attribute"""
        rect = Rectangle(20, 10, y=2)
        self.assertEqual(rect.y, 2)
        self.assertEqual(rect.x, 0)

    def test_rect_y_setter(self):
        """Test y setter method"""
        rect = Rectangle(1, 1, 0, 22, 5)
        rect.y = 55
        self.assertEqual(rect.y, 55)
        self.assertEqual(rect.x, 0)

    def test_rect_id(self):
        rect = Rectangle(20, 10, id=2)
        self.assertEqual(rect.id, 2)

    # Test private instance attribute error
    def test_rect_width_private_attr(self):
        rect = Rectangle(20, 10)
        with self.assertRaises(AttributeError):
            print(rect.__width)

    def test_rect_height_private_attr(self):
        rect = Rectangle(20, 10)
        with self.assertRaises(AttributeError):
            print(rect.__height)

    def test_rect_x_private_attr(self):
        rect = Rectangle(20, 10, 2, 4, 10)
        with self.assertRaises(AttributeError):
            print(rect.__x)

    def test_rect_y_private_attr(self):
        rect = Rectangle(20, 10, 2, 4, 10)
        with self.assertRaises(AttributeError):
            print(rect.__y)

    # None integer value as width input
    def test_width_as_string(self):
        """Test width with a string input"""
        with self.assertRaises(TypeError):
            rect = Rectangle("Python", 2)

    def test_width_as_None(self):
        """Test width with a None input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(None, 22)

    def test_width_as_inf(self):
        """Test width with an inf input """
        with self.assertRaises(TypeError):
            rect = Rectangle(float('inf'), 2)

    def test_width_as_nan(self):
        """Test width with a nan input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(float('nan'), 2)

    def test_width_as_float(self):
        """Test width with a float input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3.2, 10)

    def test_width_as_list(self):
        """Test width with a list input"""
        with self.assertRaises(TypeError):
            rect = Rectangle([2, 4, 6], 10)

    def test_width_as_dict(self):
        """Test width with a dictionary input"""
        with self.assertRaises(TypeError):
            rect = Rectangle({"name": "width", "value": 20}, 3)

    def test_width_as_tuple(self):
        """Test width with a tuple input"""
        with self.assertRaises(TypeError):
            rect = Rectangle((2,), 3)

    def test_width_as_set(self):
        """Test width with a set input"""
        with self.assertRaises(TypeError):
            rect = Rectangle({2, 4, 3, 5}, 33)

    def test_width_as_bool(self):
        """Test width with a boolean input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 2)

    def test_width_as_complex(self):
        """Test width with a complex input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(complex(5), 2)

    # Integer value <= 0 as width input
    def test_width_as_zero(self):
        """Test width with an 0 input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 3)

    def test_width_as_negative(self):
        """Test width with a negative input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-3, 10)

    # None integer value as height input
    def test_height_as_string(self):
        """Test height with a string input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, "Python")

    def test_height_as_None(self):
        """Test height with a None input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(22, None)

    def test_height_as_inf(self):
        """Test height with an inf input """
        with self.assertRaises(TypeError):
            rect = Rectangle(2, float('inf'))

    def test_height_as_nan(self):
        """Test height with a nan input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, float('nan'))

    def test_height_as_float(self):
        """Test height with a float input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 3.2)

    def test_height_as_list(self):
        """Test height with a list input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(10, [10, 12, 14, 16])

    def test_height_as_dict(self):
        """Test height with a dictionary input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, {"name": "width", "value": 20})

    def test_height_as_tuple(self):
        """Test height with a tuple input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(3, (2,))

    def test_height_as_set(self):
        """Test height with a set input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(33, {2, 4, 3, 5})

    def test_height_as_bool(self):
        """Test height with a boolean input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, False)

    def test_height_as_complex(self):
        """Test height with a complex input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(2, complex(5))

    # Integer value <= 0 as height input
    def test_height_as_zero(self):
        """Test height with an 0 input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, 0)

    def test_height_as_negative(self):
        """Test height with a negative input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(3, -10)


class TestRectangleXYAttributes(unittest.TestCase):
    """Defines test cases for x and y instance attribute value"""

    def setUp(self):
        """Setup for testing x and y attributes with
        an instance width and height attributes given
        """
        self.rect = Rectangle(10, 20)

    def tearDown(self):
        """Run a cleanup after each test case"""
        del self.rect

    # None integer value as x input
    def test_x_as_string(self):
        """Test x with a string input"""
        with self.assertRaises(TypeError):
            self.rect.x = "Not Valid"

    def test_x_as_None(self):
        """Test x with a None input"""
        with self.assertRaises(TypeError):
            self.rect.x = None

    def test_x_as_inf(self):
        """Test x with an inf input """
        with self.assertRaises(TypeError):
            self.rect.x = float('inf')

    def test_x_as_nan(self):
        """Test x with a nan input"""
        with self.assertRaises(TypeError):
            self.rect.x = float('nan')

    def test_x_as_float(self):
        """Test x with a float input"""
        with self.assertRaises(TypeError):
            self.rect.x = 3.2

    def test_x_as_list(self):
        """Test x with a list input"""
        with self.assertRaises(TypeError):
            self.rect.x = [2, 4, 6]

    def test_x_as_dict(self):
        """Test x with a dictionary input"""
        with self.assertRaises(TypeError):
            self.rect.x = {"name": "width", "value": 20}

    def test_x_as_tuple(self):
        """Test x with a tuple input"""
        with self.assertRaises(TypeError):
            self.rect.x = (2,)

    def test_x_as_set(self):
        """Test x with a set input"""
        with self.assertRaises(TypeError):
            self.rect.x = {2, 4, 3, 5}

    def test_x_as_bool(self):
        """Test x with a boolean input"""
        with self.assertRaises(TypeError):
            self.rect.x = True

    def test_x_as_complex(self):
        """Test x with a complex input"""
        with self.assertRaises(TypeError):
            self.rect.x = complex(5)

    # Integer value < 0 as x input
    def test_x_as_negative(self):
        """Test x with a negative input"""
        with self.assertRaises(ValueError):
            self.rect.x = -3

    # None integer value as y input
    def test_y_as_string(self):
        """Test y with a string input"""
        with self.assertRaises(TypeError):
            self.rect.y = "Not Valid"

    def test_y_as_None(self):
        """Test y with a None input"""
        with self.assertRaises(TypeError):
            self.rect.y = None

    def test_y_as_inf(self):
        """Test y with an inf input """
        with self.assertRaises(TypeError):
            self.rect.y = float('inf')

    def test_y_as_nan(self):
        """Test y with a nan input"""
        with self.assertRaises(TypeError):
            self.rect.y = float('nan')

    def test_y_as_float(self):
        """Test y with a float input"""
        with self.assertRaises(TypeError):
            self.rect.y = 3.2

    def test_y_as_list(self):
        """Test y with a list input"""
        with self.assertRaises(TypeError):
            self.rect.y = [2, 4, 6]

    def test_y_as_dict(self):
        """Test x with a dictionary input"""
        with self.assertRaises(TypeError):
            self.rect.y = {"name": "width", "value": 20}

    def test_y_as_tuple(self):
        """Test y with a tuple input"""
        with self.assertRaises(TypeError):
            self.rect.y = (2,)

    def test_y_as_set(self):
        """Test y with a set input"""
        with self.assertRaises(TypeError):
            self.rect.y = {2, 4, 3, 5}

    def test_y_as_bool(self):
        """Test y with a boolean input"""
        with self.assertRaises(TypeError):
            self.rect.y = True

    def test_y_as_complex(self):
        """Test y with a complex input"""
        with self.assertRaises(TypeError):
            self.rect.y = complex(5)

    # Integer value < 0 as y input
    def test_y_as_negative(self):
        """Test y with a negative input"""
        with self.assertRaises(ValueError):
            self.rect.y = -3


class TestAreaOfRectangle(unittest.TestCase):
    """Defines test case for public instance method area()."""

    def test_area_with_normal_inputs(self):
        """Test public instance area method with
        integers values that are in range of small integer"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_area_with_big_integer(self):
        """Test public instance area method with large integer"""
        rect = Rectangle(500, 1000)
        self.assertEqual(rect.area(), 500 * 1000)