#!/usr/bin/python3
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import syss

"""This module defines test cases for square module"""


class TestRectangle_init(unittest.TestCase):
    """Test cases for square instance"""

    def setUp(self):
        """Initializing instance with size parameter"""
        self.sq = Square(2)

    def tearDown(self):
        """Delete create instance"""
        try:
            os.remove("Square.json")
        except Exception:
            pass
        del self.sq

    # Test Square for empty, less, more args
    def test_sq_isinstance(self):
        """check if square an instance of rectangle """
        sq = Square(20, 10)
        self.assertIsInstance(sq, Rectangle)

    def test_sq_is_base(self):
        """check if square is instance of Base"""
        self.assertIsInstance(Square(10), Base)

    def test_no_args(self):
        """instance with no args"""
        with self.assertRaises(TypeError):
            Square()

    def test_with_excess_args(self):
        """Test with more args then required"""
        with self.assertRaises(TypeError):
            sq = Square(20, 10, 2, 3, 22)

    # Test private instance attribute error

    def test_sq_width_private_attr(self):
        sq = Square(20)
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    # Test Rectangle Instance Attribute (Getter & Setter Methods)
    def test_sq_size_attr(self):
        """Test instance width attribute"""
        self.assertEqual(self.sq.size, 2)

    def test_sq_size_setter(self):
        """Test width setter method"""
        self.sq.size = 22
        self.assertEqual(self.sq.size, 22)

    def test_sq_x_attr(self):
        """Test instance x attribute"""
        sq = Square(20, x=3)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 0)

    def test_sq_x_setter(self):
        """Test x setter method"""
        self.sq.x = 10
        self.assertEqual(self.sq.x, 10)
        self.assertEqual(self.sq.y, 0)

    def test_sq_y_attr(self):
        """Test instance y attribute"""
        sq = Square(20, 10, 2)
        self.assertEqual(sq.y, 2)
        self.assertEqual(sq.x, 10)

    def test_sq_y_setter(self):
        """Test y setter method"""
        self.sq.y = 55
        self.assertEqual(self.sq.y, 55)
        self.assertEqual(self.sq.x, 0)

    def test_sq_id(self):
        sq = Square(20, 10, id=2)
        self.assertEqual(sq.id, 2)

    def test_sq_id_two_instance(self):
        sq = Square(10, 2)
        sq2 = Square(2, 10)
        self.assertEqual(sq.id, sq2.id - 1)

    # Non-integer value as wi input
    def test_width_as_string(self):
        """Test size with a string input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle("Python", 2)
            Square("Python")

    def test_size_as_None(self):
        """Test size with a None input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle(None, 22)
            Square(None)

    def test_size_as_inf(self):
        """Test size with an inf input """
        with self.assertRaises(TypeError):
            # rect = Rectangle(float('inf'), 2)
            Square(float('inf'))

    def test_size_as_nan(self):
        """Test size with a nan input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle(float('nan'), 2)
            Square(float('nan'))

    def test_size_as_float(self):
        """Test size with a float input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle(3.2, 10)
            Square(3.2)

    def test_size_as_list(self):
        """Test size with a list input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle([2, 4, 6], 10)
            Square([2, 4, 6])

    def test_size_as_dict(self):
        """Test size with a dictionary input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle({"name": "width", "value": 20}, 3)
            Square({"name": "width", "value": 20})

    def test_size_as_tuple(self):
        """Test size with a tuple input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle((2,), 3)
            Square((2,))

    def test_size_as_set(self):
        """Test size with a set input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle({2, 4, 3, 5}, 33)
            Square({2, 4, 6, 8})

    def test_size_as_bool(self):
        """Test size with a boolean input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle(True, 2)
            Square(True)

    def test_size_as_complex(self):
        """Test size with a complex input"""
        with self.assertRaises(TypeError):
            # rect = Rectangle(complex(5), 2)
            Square(complex(5))

    # Integer value <= 0 as size input
    def test_size_as_zero(self):
        """Test size with an 0 input"""
        with self.assertRaises(ValueError):
            # rect = Rectangle(0, 3)
            Square(0)

    def test_size_as_negative(self):
        """Test size with a negative input"""
        with self.assertRaises(ValueError):
            # rect = Rectangle(-3, 10)
            Square(-5)

    # Non-integer value as x input
    def test_x_as_string(self):
        """Test x with a string input"""
        with self.assertRaises(TypeError):
            sq = Square(1, "2")

    def test_x_as_None(self):
        """Test x with a None input"""
        with self.assertRaises(TypeError):
            sq = Square(1, None)

    def test_x_as_inf(self):
        """Test x with an inf input """
        # rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.sq.x = float('inf')

    def test_x_as_nan(self):
        """Test x with a nan input"""
        # rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.sq.x = float('nan')

    def test_x_as_float(self):
        """Test x with a float input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 3.2)

    def test_x_as_list(self):
        """Test x with a list input"""
        with self.assertRaises(TypeError):
            sq = Square(1, [2, 4, 6])

    def test_x_as_dict(self):
        """Test x with a dictionary input"""
        # rect = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.sq.x = {"name": "width", "value": 20}

    def test_x_as_tuple(self):
        """Test x with a tuple input"""
        with self.assertRaises(TypeError):
            sq = Square(1, (2,))

    def test_x_as_set(self):
        """Test x with a set input"""
        # sq = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            self.sq.x = {2, 4, 3, 5}

    def test_x_as_bool(self):
        """Test x with a boolean input"""
        with self.assertRaises(TypeError):
            sq = Square(1, True)

    def test_x_as_complex(self):
        """Test x with a complex input"""
        # sq = Square(1, 2)
        with self.assertRaises(TypeError):
            self.sq.x = complex(5)

    # Integer value < 0 as x input
    def test_x_as_negative(self):
        """Test x with a negative input"""
        with self.assertRaises(ValueError):
            sq = Square(1, -2)

    # Non-integer value as y input
    def test_y_as_string(self):
        """Test y with a string input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 2, "3")

    def test_y_as_None(self):
        """Test y with a None input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 2, None)

    def test_y_as_inf(self):
        """Test y with an inf input """
        sq = Square(1, 2)
        with self.assertRaises(TypeError):
            sq.y = float('inf')

    def test_y_as_nan(self):
        """Test y with a nan input"""
        sq = Square(1, 2)
        with self.assertRaises(TypeError):
            sq.y = float('nan')

    def test_y_as_float(self):
        """Test y with a float input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 3, 3.2)

    def test_y_as_list(self):
        """Test y with a list input"""
        sq = Square(1, 3)
        with self.assertRaises(TypeError):
            sq.y = [2, 4, 6]

    def test_y_as_dict(self):
        """Test y with a dictionary input"""
        sq = Square(1, 2)
        with self.assertRaises(TypeError):
            sq.y = {"name": "width", "value": 20}

    def test_y_as_tuple(self):
        """Test y with a tuple input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 2, (2,))

    def test_y_as_set(self):
        """Test y with a set input"""
        sq = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            sq.y = {2, 4, 3, 5}

    def test_y_as_bool(self):
        """Test y with a boolean input"""
        with self.assertRaises(TypeError):
            sq = Square(1, 2, True)

    def test_y_as_complex(self):
        """Test y with a complex input"""
        sq = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            sq.y = complex(5)

    # Integer value < 0 as y input
    def test_y_as_negative(self):
        """Test y with a negative input"""
        with self.assertRaises(ValueError):
            sq = Square(1, 2, -4)


class TestSquare_update(unittest.TestCase):
    """Defines test cases for the public
       instance method -> update()
       """

    def setUp(self):
        """Setup for testing width, height x, y
        and id attributes with the update method
        """
        self.sq = Square(10, 10, 10, 10)

    def tearDown(self):
        """Run a cleanup after each test case"""
        del self.sq

        # Error checks

    def test_update_size_x_y_as_negative(self):
        """Test update with (size, x, and y)
        assignments as negative value
        """
        with self.assertRaises(ValueError):
            self.sq.update(10, -44)
            self.sq.update(10, 2, -3)
            self.sq.update(10, 2, 3, -4)

    def test_update_size_x_y_as_float(self):
        """Test update (size, x, and y)
        assignments with float values
        """
        with self.assertRaises(TypeError):
            self.sq.update(10, 2.5)
            self.sq.update(10, 2, 1.5)
            self.sq.update(10, 2, 2, 3.5)

    def test_update_size_as_zero(self):
        """Test update size assignments with 0"""
        with self.assertRaises(ValueError):
            self.sq.update(10, 0)

    def test_update_size_x_y_as_string(self):
        """Test update (size, x, and y)
        assignments with a string
        """
        with self.assertRaises(TypeError):
            self.sq.update(10, "size not valid")
            self.sq.update(10, 4, "x not valid")
            self.sq.update(10, 4, 5, "y not valid")

    def test_update_size_x_y_as_None(self):
        """Test update (size, x, and y)
        assignments as None
        """
        with self.assertRaises(TypeError):
            self.sq.update(10, None)
            self.sq.update(10, 20, None)
            self.sq.update(10, 20, 30, None)

    # Correct output checks
    def test_update_id(self):
        """Test update for correct id
        attribute assignment"""
        self.sq.update(30)
        self.assertEqual(30, self.sq.id)

    def test_update_x_y(self):
        """Test x, y values as >= 0"""
        self.sq.update(1, 1, 0)
        self.assertEqual(0, self.sq.x)

        self.sq.update(1, 1, 1, 0)
        self.assertEqual(0, self.sq.y)

        self.sq.update(1, 1, 5)
        self.assertEqual(5, self.sq.x)

        self.sq.update(2, 4, 6, 10)
        self.assertEqual(10, self.sq.y)

    def test_update_id_as_None(self):
        """Test update with None as id"""
        self.sq.update(None)
        output = "[Square] ({}) 10/10 - 10".format(self.sq.id)
        self.assertEqual(output, self.sq.__str__())

        self.sq.update(None, 2, 4, 6)
        output = "[Square] ({}) 4/6 - 2".format(self.sq.id)
        self.assertEqual(output, self.sq.__str__())

    def test_update_with_all_args(self):
        """Test update with all valid args"""
        self.sq.update(22, 20, 23, 5)
        self.assertEqual("[Square] (22) 23/5 - 20", str(self.sq))

    def test_update_with_more_args(self):
        """Test update with more than 4 args"""
        self.sq.update(22, 20, 45, 2, 3)
        self.assertEqual("[Square] (22) 45/2 - 20", str(self.sq))

        self.sq.update(89, 2, 3, 4, 5)
        self.sq.update(6, 5, 4, 3, 2)
        self.assertEqual("[Square] (6) 4/3 - 5", str(self.sq))

    # Testing kwargs key/value arguments

    # Error checks
    def test_update_kwargs_size_x_y_as_string(self):
        """Test update (size, x, y) key/value
            assignments with string as values using kwargs
            """
        with self.assertRaises(TypeError):
            self.sq.update(size="wrong type")
            self.sq.update(x="wrong input!")
            self.sq.update(y="not valid")

    def test_update_kwargs_size_x_y_as_None(self):
        """Test update (size, x, and y) key/value
        assignments as None using kwargs
        """
        with self.assertRaises(TypeError):
            self.sq.update(y=20, x=None, size=4)
            self.sq.update(y=None, size=20, x=30)
            self.sq.update(size=None, x=30, y=40)

    def test_update_kwargs_size_x_y_as_negative(self):
        """Test update with (size, x, and y)
        key/value assignments with negative value using kwargs
        """
        with self.assertRaises(ValueError):
            self.sq.update(size=10, x=-44, y=22)
            self.sq.update(x=10, y=2, size=-3)
            self.sq.update(y=-2, x=3, size=2)

    def test_update_kwargs_size_x_y_as_float(self):
        """Test update (size, x, and y) key/value
        assignments with float values using kwargs
        """
        with self.assertRaises(TypeError):
            self.sq.update(x=2.5, y=5, size=3)
            self.sq.update(size=10, x=2, y=1.5)
            self.sq.update(size=3.5, x=2, y=5)

    def test_update_kwargs_size_as_zero(self):
        """Test update size key/value
        assignments with 0 using kwargs
        """
        with self.assertRaises(ValueError):
            self.sq.update(size=0)

        # correct output tests

    def test_update_key_value_args(self):
        """Test update with **kwargs"""
        self.sq.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.sq.y)
        self.assertEqual(2, self.sq.size)
        self.assertEqual(3, self.sq.x)
        self.assertEqual(89, self.sq.id)

    def test_update_kwargs_some_wrong_keys(self):
        self.sq.update(size=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 5", str(self.sq))

        # with wrong keys
        self.sq.update(a=5, b=10)
        self.assertEqual("[Square] (89) 19/7 - 5", str(self.sq))

    def test_update_with_args_kwargs(self):
        """Test with *args and **kwargs"""
        self.sq.update(1000, y=1, sq=2, x=3, id=89)
        self.assertEqual(1000, self.sq.id)

        self.sq.update(89, 2, size=4, y=6)
        self.assertEqual("[Square] (89) 10/10 - 2", str(self.sq))


class TestSquare_str(unittest.TestCase):
    """Defines test cases for __str__method in the square class"""

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


class TestSquare_to_dictionary(unittest.TestCase):
    """Defines test cases for  to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        sq = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sq.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        sq1 = Square(10, 2, 1, 2)
        sq2 = Square(1, 2, 10)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_arg(self):
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)
