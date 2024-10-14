#!/usr/bin/python3
'''
   this module contains a function is_same_class
'''


def is_same_class(obj, a_class):
    '''
       function checks if typ(obj) is of a class
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
