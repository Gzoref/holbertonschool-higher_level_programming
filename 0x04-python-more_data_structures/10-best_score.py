#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        for key, value in a_dictionary.items():
            if value is max(a_dictionary.values()):
                return key
    else:
        return None
