#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = []
    if a_dictionary is None or a_dictionary == {}:
        return None
    else:
        for number in a_dictionary:
            biggest.append(number)
        return max(biggest)
