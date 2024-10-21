#!/usr/bin/python3
'''Module contains class Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle inheriting from Base'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''initialization of self'''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''getter function for width attr
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter for width attr
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
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

    def display(self):
        """function displays the rectangle
        """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print("{:s}{:s}".format(" " * self.__x, "#" * self.__width))

    def __str__(self):
        """function displays string rep of rectangle
        """
        return f"[Rectangle] ({self.__id}) {self.__x}/{self.__y} \
                 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """function updates attributes of rectagle with args
        """
        i = 0
        if len(args) > 0:
            for idx in args:
                if i == 0:
                    self.__id = idx
                elif i == 1:
                    self.__width = idx
                elif i == 2:
                    self.__height = idx
                elif i == 3:
                    self.__x = idx
                elif i == 4:
                    self.__y = idx
                else:
                    break
                i += 1
        else:

            for idx in kwargs:
                if idx == "id":
                    self.__id = kwargs[idx]
                elif idx == "width":
                    self.__width = kwargs[idx]
                elif idx == "height":
                    self.__height = kwargs[idx]
                elif idx == "x":
                    self.__x = kwargs[idx]
                elif idx == "y":
                    self.__y = kwargs[idx]
                else:
                    break

    def to_dictionary(self):
        """return dictionary containing atributes of rectangle
        """
        array = ["id", "width", "height", "x", "y"]
        dict = {}
        for idx in array:
            dict.update({idx: getattr(self, idx)})
        return dict
