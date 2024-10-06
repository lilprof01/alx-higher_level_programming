#!/usr/bin/python3
'''
    this module contains the function print_square
    size is the size and length of square
    raises TypeError if size is a float < 0 or not an integer
    raises a ValueError if size is < 0
'''


def print_square(size):
    '''
        this function prints a square according to the size given
        Args:
             size - is the size of square to be printed
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
