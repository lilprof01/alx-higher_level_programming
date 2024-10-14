#!/usr/bin/python3
'''
   module contains class BaseGeometry
'''


class BaseGeometry:
    '''
      class contains a geometry rep
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.value = value

        if isinstance(name, str):
            self.name = name
