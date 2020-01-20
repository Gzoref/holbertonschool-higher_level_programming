#!/usr/bin/python3
'''
Write a function that returns True
if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False.
'''


def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
