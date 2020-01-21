#!/usr/bin/python3
'''
Write a function that writes a string to a text file
(UTF8) and returns the number of characters written:
'''


def write_file(filename="", text=""):
    '''
    Write to a file
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        file_write = f.write(text)
        f.close()
        return file_write
