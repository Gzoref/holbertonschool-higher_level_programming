#!/usr/bin/python3
'''
Write a class Student that defines a student by
'''


class Student:

    def __init__(self, first_name, last_name, age):
        '''
        Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Retrieves a dictionary representation
        of a Student instance
        '''
        return vars(self)
