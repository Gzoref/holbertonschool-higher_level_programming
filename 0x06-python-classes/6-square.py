#!/usr/bin/pythpon3
"""Coordinates of a square"""


class Square:
    """Private instance attribute: size
    Instantiation with area and position method """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes attribute size """
        self.__size = size
        self.__position = position

    def area(self):
        """Calculate area of square"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Setter for square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initializes attribute size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Setter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Initializes attribute position"""
        if (value[1][0] is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[1][1] is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Print method"""
        for i in range(self.__position[1]):
            print()
        for j in range(0, self.__size):
                print(' ', end="")
                for n in range(self.__position[0]):
                    print(' ', end="")
                for m in range(self.__size):
                        print('#', end="")
                print()
        if self.size == 0:
            print('\n')
