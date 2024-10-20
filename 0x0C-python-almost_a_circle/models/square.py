#!/usr/bin/python3
"""module contains class square
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inheriting from class Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """initializing sqaure attributes
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints string representation of square instance
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter for size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square instance
        """
        if len(kwargs) != 0:
            for idx, value in kwargs.items():
                setattr(self, idx, value)
        elif len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """return dictionary containing the atributes of square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
