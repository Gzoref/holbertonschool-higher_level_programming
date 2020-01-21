#!/usr/bin/python3
'''
Write a class Student that defines a student
'''


class Student:
    '''
    Student class
    '''

    def __init__(self, first_name, last_name, age):
        '''
        Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves dict
        '''
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for items in attrs:
            if hasattr(self, items):
                my_dict[items] = getattr(self, items)
        return my_dict

    def reload_from_json(self, json):
        '''
        Replaces attributes of the Student instance
        '''
        self.__dict__.update(json)
