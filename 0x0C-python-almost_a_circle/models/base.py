#!/usr/bin/python3
'''
    this module contains class Base
'''


class Base:
    '''class Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization of class Base'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
