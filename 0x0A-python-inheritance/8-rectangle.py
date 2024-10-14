#!/usr/bin/python3
'''
   Class Rectangle
'''

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
       rectangle class inherits from BaseGeometry
    '''
    def __init__(self, width, height):
        '''
           instatition
           Args:
             width - width of rectangle
             height - height of rectangle
        '''

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
