#!/usr/bin/python3
'''
   module contains function is_kind_of_class
'''


def is_kind_of_class(obj, a_class):
    '''
       function checks if obj is a 
    '''

    if isinstance(obj, a_class):
        return True
    else:
        return False
