#!/usr/bin/python3
"""Check type"""


class Square:
    """Private instance attribute: size
    Instantiation with optional """

    def __init__(self, size=0):
        """Initializes attribute size """

        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
