#!/usr/bin/python3
'''
Write a function that creates an
Object from a “JSON file”
'''

import json


def load_from_json_file(filename):
    '''
    Create object from JSON file
    '''
    if filename is None:
        return
    with open(filename, 'r', encoding='utf-8') as f:
        json_var = json.load(f)
        return json_var
