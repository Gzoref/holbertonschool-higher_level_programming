#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area and position method """

    def __init__(self, size=0):
        """Initializes attribute size """
        self.size = size

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """Equal"""
        return self.size == other.size

    def __ne__(self, other):
        """Not Equal"""
        return self.size != other.size

    def __lt__(self, other):
        """Less than"""
        return self.size < other.size

    def __le__(self, other):
        """Less than or equal"""
        return self.size <= other.size

    def __gt__(self, other):
        """Greater than"""
        return self.size > other.size

    def __ge__(self, other):
        """Greater than or equal"""
        return self.size >= other.size
