#!/usr/bin/python3
'''
   modle contains function inherits_from
'''


def inherits_from(obj, a_class):
    '''
       function checks an obj of is instance 
    '''

    if type(obj) is not a_class:
        return True
    else:
        return False
