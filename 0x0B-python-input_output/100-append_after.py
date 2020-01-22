#!/usr/bin/python3
'''
Write a function that inserts a line of text to a file,
after each line containing a specific string (see example):
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Appends after line with string
    '''
    append_text = ""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            append_text += line
            if search_string in line:
                append_text += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(append_text)
