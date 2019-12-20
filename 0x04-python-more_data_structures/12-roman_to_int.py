#!/usr/bin/python3
def roman_to_int(roman_string):
        roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}
        result = 0
        item = 0
        roman = roman_string
        if type(roman) is not str or len(roman) is 0:
                return 0
        for item in range(item, len(roman)):
                if item < len(roman) - 1\
                   and\
                   roman_dictionary[roman[item]] <\
                   roman_dictionary[roman[item + 1]]:
                    result -= roman_dictionary[roman[item]]
                else:
                    result += roman_dictionary[roman[item]]
        return result
