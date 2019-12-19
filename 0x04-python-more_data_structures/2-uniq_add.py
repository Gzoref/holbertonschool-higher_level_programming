#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniqueList = set(my_list)
    for number in uniqueList:
        sum += number
    return sum
