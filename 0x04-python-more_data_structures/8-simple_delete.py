#!/usr/bin/python3

# A function that deletes a key in a dictionary.
def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key)!= None:
        del a_dictionary[key]
    return (a_dictionary)