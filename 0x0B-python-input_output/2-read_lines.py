#!/usr/bin/python3
'''
Write a function that reads n lines of a text file
(UTF8) and prints it to stdout:
'''


def read_lines(filename="", nb_lines=0):
    line_count = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
            print(line, end='')
            if nb_lines == line_count:
                break
