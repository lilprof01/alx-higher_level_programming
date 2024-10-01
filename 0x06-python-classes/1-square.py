#!/usr/bin/python3
'''1-square.py
    a class that defines the sie of a square
'''


square = __import__("0-square").Square


class Square(square):
    """an inherited class from Square definition class
    Args:
        square(class): a class which defines a square
    """

    def __init__(self, size):
        """initialization function
        Args:
            size(int): a size attribute initialized
        """
        self.__size = size
