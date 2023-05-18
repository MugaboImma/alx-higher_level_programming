#!/usr/bin/python3

# A function that replaces all occurrences of an element by
# another in a new list.

def search_replace(my_list, search, replace):
    nw_list = list(map(lambda x: replace if x == search else x, my_list))
    return (nw_list)
