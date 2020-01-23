#!/usr/bin/python3
'''
Create a folder named models with an empty file __init__.py
inside - with this file, the folder will become a Python module
'''

class Base:
    '''
    Base class
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
