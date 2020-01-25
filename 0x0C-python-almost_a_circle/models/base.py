#!/usr/bin/python3
'''
Create a folder named models with an empty file __init__.py
inside - with this file, the folder will become a Python module
'''
import json


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

    def to_json_string(list_dictionaries):
        '''
        Turn dictionary representation
        into JSON
        '''
        if list_dictionaries is None:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves JSON of dictionary
        to a file <Class name>.json
        '''
        listToDictionary = []
        if not list_objs:
            list_objs = []
        for items in list_objs:
            listToDictionary.append(items.to_dictionary())
        
        with open('{}'.format(cls.__name__), 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(listToDictionary))
        