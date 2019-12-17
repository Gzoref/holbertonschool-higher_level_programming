#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if not my_list:
        return None
    else:
        for num in my_list:
            if largest < num:
                largest = num
        return largest
