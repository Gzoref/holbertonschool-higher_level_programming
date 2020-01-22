#!/usr/bin/python3
'''
Write a class Square that inherits
from Rectangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        '''
        Constructor
        '''
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        '''
        String representation
        '''
        return '[Square] {}/{}'.format(self.__size, self.__size)
