#!/usr/bin/python3

# A function that returns a new dictionary with all values multiplied by 2
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    list_keys = list(new_dict.keys())

    for i in list_keys:
        new_dict[i] *= 2

    return (new_dict)
