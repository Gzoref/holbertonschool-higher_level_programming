#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for k, v in a_dictionary.items():
        if value is v:
            new_list.append(k)
    if len(new_list) > 0:
        for new in new_list:
            del a_dictionary[new]
    return a_dictionary
