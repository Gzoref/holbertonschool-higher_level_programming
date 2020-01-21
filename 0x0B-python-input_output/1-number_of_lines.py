#!/usr/bin/python3
'''
Write a function that returns the number
of lines of a text file
'''


def number_of_lines(filename=""):
    line_count = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line_count += 1
    return line_count
