#!/usr/bin/python3
'''
Write the class Square that
inherits from Rectangle:
'''
from models.base import Base

class Square(Rectangle):
    '''
    Square class inherits from Rectangle
    '''

    def __init__(self, size, x=0, y=0, id=None):
        super()__init__(size, size, x, y, id)
        self.size = size