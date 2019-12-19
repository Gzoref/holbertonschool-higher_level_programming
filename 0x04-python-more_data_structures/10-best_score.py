#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    biggest = []
    for number in a_dictionary:
        biggest.append(number)
    return max(biggest)
