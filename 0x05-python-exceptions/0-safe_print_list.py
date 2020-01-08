#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for items in range(x):
        try:
            index = 0
            print("{}".format(my_list[items]), end='')
        except IndexError:
            break
