#!/usr/bin/python3
'''module contains class rectangle
'''


class Rectangle:
    '''defines a class rectangle
    '''

    def __init__(self, width=0, height=0):
        '''initializing object
           Args:
               width - width of rectangle (defaults to 0)
               height - height of rectangle (defaults to 0)
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''width property
        returns:
           width(int) - private atrribute
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''width setter
        Args:
            value(int) - width of rectangle
        Raises:
            TypeError: width must be an integer
            TypeError: width must be >= 0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property
        Returns:
            height(int) - private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            value (int) - height of rectangle
        Raises:
            TypeError: height must be an integer
            TypeError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''calculates area of the rectangle
        Returns:
            (int) - area of rectangle
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''calculates perimeter of the rectangle
        Returns:
             (int) - perimeter of rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''creates a string representation of the rectangle
        '''
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            if i == self.__height - 1:
                rectangle_str += "#" * self.__width
            else:
                rectangle_str += "#" * self.__width + "\n"
        return rectangle_str        
