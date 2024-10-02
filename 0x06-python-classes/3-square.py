#!/usr/bin/python3
"""3-square.py
    a class to define a size of square
"""


square = __import__("2-square").Square


class Square():
    """ a class that defines and calculate area of the square
    Args:
        square(class): a class which define a square with size
    """

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

    def area(self):
        """calculating the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2
