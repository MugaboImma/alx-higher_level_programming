#!/usr/bin/python3

# A function that adds all unique integers in a list
#(only once for each integer).

def uniq_add(my_list=[]):
    unique_list = set(my_list)
    n = 0

    for i in unique_list:
        n += i

    return (n)
