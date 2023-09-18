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

    # None integer values
    def test_width_as_string(self):
        rect = Rectangle("Python", 3)
