#!/usr/bin/python3
"""5-square.py
    a class to define a size of square
"""


class Square():
    """a class to define and calculate area of the square
    Args:
        square(class): a class which define a square with size
    """

    def __init__(self, size=0, position=(0, 0)):
        """initializing square

        Args:
            size(int): the size of the square passed. Defaults to 0.

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        self.__size = size
        self.__position = position
        error = 'position must be a tuple of 2 positive integers'

        try:
            if position[1]:
                pass
        except IndexError:
            raise TypeError(error)

        for pos in self.__position:
            if type(pos) != int:
                raise TypeError(error)
            elif pos < 0:
                raise ValueError(error)

        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """getter for size

        Returns:
            integer: sends the value of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size

        Args:
            value(int): a new size value

        Raises:
            TypeError: if not integer
            ValueError: if < 0
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """calculating the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size**2

    def my_print(self):
        """printing square"""
        if self.__size == 0:
            print()
            return
        print('\n'*self.__position[1], end="")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(' ', end="")
            for j in range(self.__size):
                print('#', end="")
            print()

    @property
    def position(self):
        return self.__position
