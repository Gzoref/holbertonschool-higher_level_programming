#!/usr/bin/python3
'''
Write a function that returns an object
(Python data structure) represented by a
JSON string:
'''

import json


def from_json_string(my_str):
    '''
    Return object as JSON
    '''
    try:
        json_var = json.loads(my_str)
    except ValueError:
        raise ValueError('Expecting property name enclosed in double quotes:')
    return json_var
