#!/usr/bin/python3
'''
Write a class Square that inherits 
from Rectangle (9-rectangle.py). 
(task based on 10-square.py).
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def area(self):
        return self.size ** 2

    def __str__(self):
        return '[Square] {}/{}'.format(self.__size)
