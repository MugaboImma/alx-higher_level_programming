#!/usr/bin/python3

# A function that returns the number of keys in a dictionary.
def number_keys(a_dictionary):
    n = 0
    list_of_keys = list(a_dictionary.keys())

    for i in list_of_keys:
        n += 1
    return (n)

