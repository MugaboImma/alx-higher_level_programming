#!/usr/bin/python3

""" a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer."""

def roman_to_int(roman_string: str):
    
    if (roman_string) is None or type(roman_string) != str:
        return 0
    dict_num = {'I': 1, 'V': 5, 'X': 10, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    num = [dict_num[i] for i in roman_string] + [0]
    rep = 0

    for j in range(len(num) - 1):
        if num[j] >= num[j+1]:
            rep += num[j]
        else:
            rep -= num[j]

    return (rep)
