#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys

"""This module defines test cases for the rectangle module"""


class TestRectangle_init(unittest.TestCase):
    """Test cases for rectangle instance"""

    # Test Rectangle for empty, less, more args
    def test_rect_isinstance(self):
        """check if Rectangle inherits from base"""
        rect = Rectangle(20, 10)
        self.assertIsInstance(rect, Base)

    def test_no_args(self):
        """instance with no args"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_with_arg(self):
        """instance with one arg"""
        with self.assertRaises(TypeError):
            Rectangle(2)

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

    # Non-integer value as width input
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

    # Non-integer value as height input
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


class TestRectangle_validate_attributes(unittest.TestCase):
    """Defines test cases for x and y instance attribute value"""

    # Non-integer value as x input
    def test_x_as_string(self):
        """Test x with a string input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, "3")

    def test_x_as_None(self):
        """Test x with a None input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, None)

    def test_x_as_inf(self):
        """Test x with an inf input """
        rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            rect.x = float('inf')

    def test_x_as_nan(self):
        """Test x with a nan input"""
        rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            rect.x = float('nan')

    def test_x_as_float(self):
        """Test x with a float input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3.2)

    def test_x_as_list(self):
        """Test x with a list input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, [2, 4, 6])

    def test_x_as_dict(self):
        """Test x with a dictionary input"""
        rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            rect.x = {"name": "width", "value": 20}

    def test_x_as_tuple(self):
        """Test x with a tuple input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, (2,))

    def test_x_as_set(self):
        """Test x with a set input"""
        rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            rect.x = {2, 4, 3, 5}

    def test_x_as_bool(self):
        """Test x with a boolean input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, True)

    def test_x_as_complex(self):
        """Test x with a complex input"""
        rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            rect.x = complex(5)

    # Integer value < 0 as x input
    def test_x_as_negative(self):
        """Test x with a negative input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, -3)

    # Non-integer value as y input
    def test_y_as_string(self):
        """Test y with a string input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, "4")

    def test_y_as_None(self):
        """Test y with a None input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, None)

    def test_y_as_inf(self):
        """Test y with an inf input """
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = float('inf')

    def test_y_as_nan(self):
        """Test y with a nan input"""
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = float('nan')

    def test_y_as_float(self):
        """Test y with a float input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, 3.2)

    def test_y_as_list(self):
        """Test y with a list input"""
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = [2, 4, 6]

    def test_y_as_dict(self):
        """Test x with a dictionary input"""
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = {"name": "width", "value": 20}

    def test_y_as_tuple(self):
        """Test y with a tuple input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, (2,))

    def test_y_as_set(self):
        """Test y with a set input"""
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = {2, 4, 3, 5}

    def test_y_as_bool(self):
        """Test y with a boolean input"""
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 2, 3, True)

    def test_y_as_complex(self):
        """Test y with a complex input"""
        rect = Rectangle(1, 2, 3)
        with self.assertRaises(TypeError):
            rect.y = complex(5)

    # Integer value < 0 as y input
    def test_y_as_negative(self):
        """Test y with a negative input"""
        with self.assertRaises(ValueError):
            rect = Rectangle(1, 2, 3, -4)


class TestRectangle_area(unittest.TestCase):
    """Defines test cases for public instance method area()."""

    def test_area_with_normal_inputs(self):
        """Test public instance area method with
        integers values that are in range of small integer"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

    def test_area_with_big_integer(self):
        """Test public instance area method with large integer"""
        rect = Rectangle(500, 1000)
        self.assertEqual(rect.area(), 500 * 1000)


class TestRectangle_display(unittest.TestCase):
    """Defines test cases for the public
    instance method -> display()
    """
    @staticmethod
    def screenshotStdout(rect_instance):
        """Capture / screenshot the stdout
        and return the text printed.

        Arg: Rectangle instance to print to stdout.
        Returns: Screenshot of the text printed to the stdout
        """
        output_screenshot = StringIO()
        sys.stdout = output_screenshot
        rect_instance.display()
        sys.stdout = sys.__stdout__
        return output_screenshot

    def test_display_square_size(self):
        """Test correct square output."""
        rect = Rectangle(2, 3)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        self.assertEqual("##\n##\n##\n", screenshot.getvalue())

    def test_display_square_size_2(self):
        """Test correct square output."""
        rect = Rectangle(3, 2)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        output = "###\n###\n"
        self.assertEqual(output, screenshot.getvalue())

    def test_display_square_large(self):
        """Test correct square output."""
        rect = Rectangle(10, 5)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(output, screenshot.getvalue())

    def test_display_square_with_x(self):
        """Test correct square output"""
        rect = Rectangle(3, 2, 1)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        self.assertEqual(" ###\n ###\n", screenshot.getvalue())

    def test_display_square_with_y(self):
        """Test correct square output"""
        rect = Rectangle(4, 5, 0, 1)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        output = "\n####\n####\n####\n####\n####\n"
        self.assertEqual(output, screenshot.getvalue())

    def test_display_square_with_x_y(self):
        """Test correct square output"""
        rect = Rectangle(2, 4, 3, 2)
        screenshot = TestRectangle_display.screenshotStdout(rect)
        output = "\n\n   ##\n   ##\n   ##\n   ##\n"
        self.assertEqual(output, screenshot.getvalue())


class TestRectangle_str(unittest.TestCase):
    """Defines test cases for __str__method """

    @staticmethod
    def screenshotStdout(rect_instance):
        """Capture / screenshot the stdout
        and return the text printed.

        Arg: Rectangle instance to print to stdout.
        Returns: Screenshot of the text printed to the stdout
        """
        output_screenshot = StringIO()
        sys.stdout = output_screenshot
        print(rect_instance)
        sys.stdout = sys.__stdout__
        return output_screenshot

    def test_str_method(self):
        """Test correct print output"""
        rect = Rectangle(10, 5, id=20)
        screenshot = TestRectangle_str.screenshotStdout(rect)
        output = "[Rectangle] (20) 0/0 - 10/5\n"
        self.assertEqual(output, screenshot.getvalue())

    def test_str_method_with_x_y(self):
        """Test correct print output with x and y given"""
        rect = Rectangle(18, 12, 5, 4)
        screenshot = TestRectangle_str.screenshotStdout(rect)
        output = "[Rectangle] ({}) 5/4 - 18/12\n".format(rect.id)
        self.assertEqual(output, screenshot.getvalue())

    def test_str_method_wth_x_y_id(self):
        """Test correct print output with x, y, id"""
        rect = Rectangle(2, 5, 7, 3, 22)
        self.assertEqual("[Rectangle] (22) 7/3 - 2/5", rect.__str__())


class TestSquare_str(unittest.TestCase):
    """Defines test cases for __str__method in square"""

    @staticmethod
    def screenshotStdout(rect_instance):
        """Capture / screenshot the stdout
        and return the text printed.

        Arg: Square instance to print to stdout.
        Returns: Screenshot of the text printed to the stdout
        """
        output_screenshot = StringIO()
        sys.stdout = output_screenshot
        print(rect_instance)
        sys.stdout = sys.__stdout__
        return output_screenshot

    def test_str_method(self):
        """Test correct print output"""
        sq = Square(10, 5, id=20)
        screenshot = TestSquare_str.screenshotStdout(sq)
        output = "[Square] (20) 5/0 - 10\n"
        self.assertEqual(output, screenshot.getvalue())

    def test_str_method_with_x_y(self):
        """Test correct print output with x and y given"""
        sq = Square(18, 12, 5)
        screenshot = TestSquare_str.screenshotStdout(sq)
        output = "[Square] ({}) 12/5 - 18\n".format(sq.id)
        self.assertEqual(output, screenshot.getvalue())

    def test_str_method_wth_x_y_id(self):
        """Test correct print output with x, y, id"""
        sq = Square(2, 5, 7, 3)
        self.assertEqual("[Square] (3) 5/7 - 2", sq.__str__())

    def test_str_method_with_size(self):
        """Test with size only"""
        sq = Square(5)
        screenshot = TestSquare_str.screenshotStdout(sq)
        output = "[Square] ({}) 0/0 - 5\n".format(sq.id)
        self.assertEqual(output, screenshot.getvalue())


class TestRectangle_update(unittest.TestCase):
    """Defines test cases for the public
    instance method -> update()
    """

    def setUp(self):
        """Setup for testing width, height x, y
        and id attributes with the update method
        """
        self.rect = Rectangle(10, 10, 10, 10, 10)

    def tearDown(self):
        """Run a cleanup after each test case"""
        del self.rect

    # Error checks
    def test_update_width_height_x_y_as_negative(self):
        """Test update with (width, height, x, and y)
        assignments as negative value
        """
        with self.assertRaises(ValueError):
            self.rect.update(10, -44)
            self.rect.update(10, 2, -3)
            self.rect.update(10, 2, 3, -2)
            self.rect.update(10, 2, 3, 2, -5)

    def test_update_width_height_x_y_as_float(self):
        """Test update (width, height, x, and y)
        assignments with float values
        """
        with self.assertRaises(TypeError):
            self.rect.update(10, 2.5)
            self.rect.update(10, 2, 1.5)
            self.rect.update(10, 2, 5, 3.5)
            self.rect.update(10, 2, 5, 3, 7.2)

    def test_update_width_height_as_zero(self):
        """Test update width and height assignments with 0"""
        with self.assertRaises(ValueError):
            self.rect.update(10, 0)
            self.rect.update(10, 5, 0)

    def test_update_width_height_x_y_as_string(self):
        """Test update (width, height, x, and y)
        assignments with a string
        """
        with self.assertRaises(TypeError):
            self.rect.update(10, "WIDTH NOT VALID")
            self.rect.update(10, 4, "Not valid")
            self.rect.update(10, 4, 5, "x not valid")
            self.rect.update(10, 4, 5, 6, "y not valid")

    def test_update_width_height_x_y_as_None(self):
        """Test update (width, height, x, and y)
        assignments as None
        """
        with self.assertRaises(TypeError):
            self.rect.update(20, None)
            self.rect.update(20, 30, None)
            self.rect.update(20, 30, 40, None)
            self.rect.update(20, 30, 40, 50, None)

    # Correct output checks
    def test_update_id_as_None(self):
        """Test update with None as id"""
        rect = Rectangle(10, 10, 10, 10, 10)
        rect.update(None)
        output = "[Rectangle] ({}) 10/10 - 10/10".format(rect.id)
        self.assertEqual(output, rect.__str__())

        r = Rectangle(10, 10, 10, 10)
        r.update(None, 2, 4, 6)
        output = "[Rectangle] ({}) 6/10 - 2/4".format(r.id)
        self.assertEqual(output, r.__str__())

    def test_update_id(self):
        """Test update for correct id
        attribute assignment"""
        self.rect.update(30)
        self.assertEqual(30, self.rect.id)

    def test_update_x_y(self):
        """Test x, y values as >= 0"""
        self.rect.update(1, 1, 1, 0)
        self.assertEqual(0, self.rect.x)

        self.rect.update(1, 1, 1, 1, 0)
        self.assertEqual(0, self.rect.y)

        self.rect.update(1, 1, 1, 5)
        self.assertEqual(5, self.rect.x)

        self.rect.update(2, 4, 6, 8, 10)
        self.assertEqual(10, self.rect.y)

    def test_update_with_all_args(self):
        """Test update with all valid args"""
        self.rect.update(22, 20, 23, 5, 60)
        self.assertEqual("[Rectangle] (22) 5/60 - 20/23", str(self.rect))

    def test_update_with_more_args(self):
        """Test update with more than 5 args"""
        self.rect.update(22, 20, 45, 2, 3, 15)
        self.assertEqual("[Rectangle] (22) 2/3 - 20/45", str(self.rect))

        self.rect.update(89, 2, 3, 4, 5, 6)
        self.rect.update(6, 5, 4, 3, 2, 89)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(self.rect))

    # Testing kwargs key/value arguments

    # Error checks
    def test_update_kwargs_width_height_x_y_as_string(self):
        """Test update (width, height, x, y) key/value
        assignments with string as values using kwargs
        """
        with self.assertRaises(TypeError):
            self.rect.update(width="wrong type")
            self.rect.update(height="invalid")
            self.rect.update(x="wrong input!")
            self.rect.update(y="not valid")

    def test_update_kwargs_width_height_x_y_as_None(self):
        """Test update (width, height, x, and y) key/value
        assignments as None using kwargs
        """
        with self.assertRaises(TypeError):
            self.rect.update(y=20, x=None, height=3, width=4)
            self.rect.update(y=None, x=20, height=30, width=3)
            self.rect.update(y=20, x=30, height=40, width=None)
            self.rect.update(height=None, width=22, x=20, y=30)

    def test_update_kwargs_width_height_x_y_as_negative(self):
        """Test update with (width, height, x, and y)
        key/value assignments with negative value using kwargs
        """
        with self.assertRaises(ValueError):
            self.rect.update(width=10, x=-44, height=20, y=22)
            self.rect.update(height=10, x=2, width=-3)
            self.rect.update(height=2, width=3, y=-2)
            self.rect.update(height=-10, x=2, y=3, width=2)

    def test_update_kwargs_width_height_x_y_as_float(self):
        """Test update (width, height, x, and y) key/value
        assignments with float values using kwargs
        """
        with self.assertRaises(TypeError):
            self.rect.update(x=2.5, y=5, height=3, width=2)
            self.rect.update(height=10, width=2, y=1.5)
            self.rect.update(width=3.5, x=2, height=5)
            self.rect.update(x=10, height=2.5, width=2, y=3)

    def test_update_kwargs_width_height_as_zero(self):
        """Test update width and height key/value
        assignments with 0 using kwargs
        """
        with self.assertRaises(ValueError):
            self.rect.update(width=10, height=0)
            self.rect.update(height=10, width=0)

    # correct output tests
    def test_update_key_value_args(self):
        """Test update with **kwargs"""
        self.rect.update(y=1, width=2, x=3, id=89)
        self.assertEqual(1, self.rect.y)
        self.assertEqual(2, self.rect.width)
        self.assertEqual(3, self.rect.x)
        self.assertEqual(89, self.rect.id)

    def test_update_kwargs_some_wrong_keys(self):
        self.rect.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(self.rect))

        # with wrong keys
        self.rect.update(a=5, b=10)
        self.assertEqual("[Rectangle] (89) 19/7 - 10/5", str(self.rect))

    def test_update_with_args_kwargs(self):
        """Test with *args and **kwargs"""
        self.rect.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.rect.id)

        self.rect.update(89, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (89) 10/10 - 2/10", str(self.rect))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Defines tests for the public
       instance to_dictionary method
    """

    # Error check
    def test_to_dict_missing_args(self):
        """Testing with empty argument"""
        with self.assertRaises(TypeError):
            Rectangle()
            Rectangle(1)

    def test_to_dict_type(self):
        """Testing the type  the method will return
        when use with the type function"""
        rect = Rectangle(100, 33)
        self.assertEqual(type(rect.to_dictionary()), dict)

    # Output check
    def test_to_dict_output(self):
        """Testing correct output of an instance"""
        rect = Rectangle(10, 20, 6, 33, 3)
        output = {'x': 6, 'width': 10, 'id': 3, 'height': 20, 'y': 33}
        self.assertEqual(output, rect.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)
