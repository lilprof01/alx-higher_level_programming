#!/usr/bin/python3
'''
    this module contains function say_my_name
'''


def say_my_name(first_name, last_name=""):
    '''
        this function computes and prints a persons name
        Args:
            first_name - first input(string)
            last_name - second input(string)
        if first_name is not a string, function raises TypeError
        if last_name is not a string, function raises a TypeError
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
