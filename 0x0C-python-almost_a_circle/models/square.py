#!/usr/bin/python3
"""Module that has square childclass"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Childclass that inherits from Base class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding str method"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that updates attributes"""
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """square dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
