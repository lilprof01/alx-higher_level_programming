#!/usr/bin/python3
'''unittest module for base
'''


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    '''unittest for class Base
    '''

    def setup(self):
        '''sets up Base for test'''
        Base._Base__nb_objects = 0
        pass

    def teardown(self):
        '''cleans up after each test'''
        pass

    def test_private(self):
        '''Tests if nb_objects is a private class attribute'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_initialization(self):
        '''Tests if nb_objects initializes to zero on setup'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_instance_without_setId(self):
        '''Tests instance without a set id'''
        a = Base()
        b = Base()
        self.assertEqual(a.id, 1)
        self.assertEqual(b.id, 2)

    def test_instance_with_setId(self):
        '''tests for an instance with a set id'''
        a = Base(15)
        self.assertEqual(a.id, 15)


if __name__ == "__main__":
    unittest.main()
