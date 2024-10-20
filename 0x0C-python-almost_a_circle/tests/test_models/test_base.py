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

    def test_if_nb_objects_private(self):
        '''Tests if nb_objects is a private class attribute'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_if_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero on setup'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)
