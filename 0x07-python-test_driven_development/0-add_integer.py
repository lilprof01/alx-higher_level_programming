#!/usr/bin/python3
'''
this module contains the funtcion add_integer
    args: a - first integer
          b - second integer
'''


def add_integer(a, b=98):
    '''
     function adds two integers
    '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
