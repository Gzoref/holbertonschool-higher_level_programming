#!/usr/bin/python3


"""Say my name"""


def say_my_name(first_name, last_name=""):
    """Function thats prints my name"""
    try:
        return first_name + ' ' + last_name
    except:
        if isinstance(first_name, str):
            raise TypeError('first_name must be a string')
        if isinstance(last_name, str):
            raise TypeError('last_name must be a string')
