#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test max_integer function using unit tests."""

    def test_empty_list(self):
        """Test for when an empty
           list is passed to the function.
        """
        self.assertIsNone(max_integer([]))

    def test_empty_string(self):
        """Test for when am empty string
           is passed in as argument
        """
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """Test list of string."""
        list_of_strings = ["Unit", "testing", "is", "cool"]
        self.assertEqual(max_integer(list_of_strings), "testing")

    def test_single_string(self):
        """Test a string."""
        name = "Gbaboh"
        self.assertEqual(max_integer(name), 'o')

    def test_no_args(self):
        """Test for when no is argrument passed"""
        self.assertIsNone(max_integer())

    def test_wrong_type(self):
        """Test for values that are
           not integer in the list
        """
        with self.assertRaises(TypeError):
            max_integer([3, "Unit", 4, 2])

    def test_floats(self):
        """Test floats numbers"""
        numbers = [2.3, 5.6, 8.6, 1.4, -6.6]
        self.assertEqual(max_integer(numbers), 8.6)

    def test_negatives_values(self):
        """Test for negative values"""
        self.assertEqual(max_integer([-30, -33, -2, -10]), -2)

    def test_integers_and_floats(self):
        """Test int and floats numbers"""
        numbers = [2.3, 8.6, 4, 10]
        self.assertEqual(max_integer(numbers), 10)

    def test_none_value(self):
        """
        Test for when None is
        passed as an arugment
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_valid_output(self):
        """Test valid argument that
           is expected to be successful
        """
        self.assertEqual(max_integer([2, 5, 30, 80, -4, 20]), 80)

    def test_one_value(self):
        """Test when list contains one value"""
        self.assertEqual(max_integer([2]), 2)

    def test_equal_inputs(self):
        """Test all inputs values are equal"""
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_max_value_at_begining(self):
        """Test for when first value is max"""
        self.assertEqual(max_integer([10, 4, 4, 4]), 10)
