#!/usr/bin/python3
'''
Write a function that appends a string
at the end of a text file (UTF8) and returns
the number of characters added
'''


def append_write(filename="", text=""):
    '''
    Append to a file
    '''
    with open(filename, 'a+', encoding='utf-8') as f:
        append_file = f.write(text)
        f.close()
        return append_file
