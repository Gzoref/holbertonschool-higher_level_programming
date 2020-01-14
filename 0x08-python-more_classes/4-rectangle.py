#!/usr/bin/python3
"""
Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes private attribute width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """
        width getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        width setter
        """
        if not isinstance(value, int):
            TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__height = value

    def area(self):
        """
        Returns a rectangle's area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns a rectangle's perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        String represenation
        """
        string = ""
        for i in range(self.height):
            string += '#' * self.width + '\n'
        return string[:-1]

    def __repr__(self):
        """
        Representation
        """
        return "Rectangle({}, {})".format(self.width, self.height)
