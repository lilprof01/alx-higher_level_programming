#!/usr/bin/python3
'''2-square.py
    this class defines the size of a square
'''


square = __import__("1-square").Square


class Square(square):
    '''a class to define and calculate area of the square
    Args:
        square(class): a class which define a square with size
    '''

    def __init__(self, size=0):
        """initializing square

        Args:
            size(int): the size of the square passed. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')
