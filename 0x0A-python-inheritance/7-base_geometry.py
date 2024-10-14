#!/usr/bin/python3
'''
   module contains class BaseGeometry
'''


class BaseGeometry:
    '''
      class contains a geometry rep
    '''

    def area(self):
        """area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
