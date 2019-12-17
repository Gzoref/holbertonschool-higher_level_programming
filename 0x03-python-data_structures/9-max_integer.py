#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if len(my_list) < 1:
        return None
    else:
        for num in my_list:
            if largest < num:
                largest = num
        return largest
