#!/usr/bin/python3
"""module contains a class TestRectangleMethods"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ Defines tests for Rectangle class """

    @classmethod
    def setUp(self):
        """ Runs for each test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_docstring(self):
        """ Test if docstring is present """
        self.assertIsNotNone(Rectangle.__doc__)

    def test_random_id(self):
        """ Test random arguments passed """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        r4 = Rectangle(2, 10)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r4.id, 3)

    def test_class(self):
        """ Test Rectangle class type """
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_inheritance(self):
        """ Test if Rectangle inherits from Base """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_arg(self):
        """ Test for passing one or no argument """
        with self.assertRaises(TypeError):
            Rectangle(20)
            Rectangle()

    def test_constructor_no_args_passed(self):
        """ Test constructor with no argument"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_one_arg_passed(self):
        """ Test constructor with one argument """
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(e.exception), s)

    def test_width_and_height_types(self):
        """ Test for width and height types"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Chris", 9)
            Rectangle('c', 9)
            Rectangle(True, 8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, "Breezy")
            Rectangle(7, 'c')
            Rectangle(True, 6)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(5, 4, "CB")
            Rectangle(5, 4, 'c')
            Rectangle(True, 2, 4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 1, 'c')
            Rectangle(3, 2, 1, "CB")
            Rectangle(True, 1, 2, 3)

    def test_width_and_height_range(self):
        """ Test for width and height ranges"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-7, 2)
            Rectangle(0, 1)
            Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(6, -5)
            Rectangle(2, 0)
            Rectangle(1, 0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 4, -2)
            Rectangle(13, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(7, 6, 5, -5)
            Rectangle(4, 2, 1, 0)

    def test_area(self):
        """ Test area """
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 2 * 3)
        self.assertEqual(r2.area(), 2 * 10)
        self.assertEqual(r3.area(), 8 * 7)

    def test_area_return(self):
        """ Checking the return value of area method """
        r1 = Rectangle(2, 2)
        self.assertEqual(r1.area(), 4)
        r1.width = 5
        self.assertEqual(r1.area(), 10)
        r1.height = 5
        self.assertEqual(r1.area(), 25)

    def test_area_with_no_args(self):
        """ Test area method with no arguments """
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
