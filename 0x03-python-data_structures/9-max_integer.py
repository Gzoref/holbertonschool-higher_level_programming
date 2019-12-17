#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if my_list is None or len(my_list) == 0:
        return None
    else:
        largest = my_list.copy()
        largest.sort()
    return largest[-1]
