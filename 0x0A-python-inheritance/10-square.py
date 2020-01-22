#!/usr/bin/python3
'''
Write a class Square that inherits
from Rectangle (9-rectangle.py):
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
