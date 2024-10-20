#!/usr/bin/python3
'''Module contains class Rectangle'''


from models.base import Base

class Rectangle(Base):
    '''class Rectangle inheriting from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization of self'''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter function for width attr
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width attr
        '''
        self.__width = value

    @property
    def height(self):
        '''getter for height attr
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter for height attr
        '''
        self.__height = value

    @property
    def x(self):
        """getter function for attr x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter function for attr x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """getter function for attr y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter function for attr y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """function returns area of rectangle
        """
        return self.__width * self.__height
