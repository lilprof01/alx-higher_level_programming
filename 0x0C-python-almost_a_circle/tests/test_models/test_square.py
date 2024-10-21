#!/usr/bin/python3
"""Defines a class TestSquareMethods"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """ Defines tests for Square class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def tearDown(self):
        """ Cleans up after each test """
        pass

    def test_square(self):
        """ Test new square """
        s1 = Square(3)
        s2 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.size, 1)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 3)
        self.assertEqual(s2.id, 4)

    def test_attributes_types(self):
        """ Test for width and x and y types"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("1")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "2")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "3")

    def test_attribute_ranges(self):
        """ Test for width and height ranges"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -3)

    def test_constructor_with_no_args(self):
        """ Tests constructor with no args """
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_constructor_with_many_args(self):
        """ Tests constructor with many arguments """
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_is_Rectangle_instance(self):
        """ Test Square is a Rectangle instance """
        s1 = Square(1)
        self.assertEqual(True, isinstance(s1, Rectangle))

    def test_area(self):
        """ Test area method """
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_area_size(self):
        """ Test area method after modifying size """
        r1 = Square(4)
        self.assertEqual(r1.area(), 16)
        r1.size = 9
        self.assertEqual(r1.area(), 81)

    def test_area_with_no_args(self):
        """ Test area method with no arguments"""
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), s)
