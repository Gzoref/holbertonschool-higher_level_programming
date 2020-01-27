#!/usr/bin/python3
'''
Create a folder named models with an empty file __init__.py
inside - with this file, the folder will become a Python module
'''
import json
import csv


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

    def from_json_string(json_string):
        '''
        Returns list of
        dictionaries from JSON
        '''
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Saves JSON of dictionary
        to a file <Class name>.json
        '''
        listdict = []
        if not list_objs:
            list_objs = []
        for items in list_objs:
            listdict.append(items.to_dictionary())

        with open('{}.json'.format(cls.__name__), 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(listdict))

    @classmethod
    def create(cls, **dictionary):
        '''
        Returns instance with
        all attributes set
        '''
        newInstance = cls(1, 1)
        newInstance.update(**dictionary)
        return newInstance

    @classmethod
    def load_from_file(cls):
        '''
        Returns a list
        of instances
        '''
        insanceList = []
        try:
            with open('{}'.format(cls.__name__), 'r', encoding='utf-8') as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            insanceList.append(cls.create(**dictionary))
        return insanceList

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Wrte to csv
        '''
        listToDictionary = []
        if list_objs is not None:
            list_objs = []
        for items in list_objs:
            listToDictionary.append(items.to_dictionary())

        with open('{}.csv'.format(cls.__name__), 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''
        Returns a list
        of instances
        '''
        insanceList = []
        try:
            with open('{}'.format(cls.__name__), 'r', encoding='utf-8') as f:
                objectList = cls.from_json_string(f.read())
        except IOError:
            return []
        for dictionary in objectList:
            insanceList.append(cls.create(**dictionary))
        return insanceList
