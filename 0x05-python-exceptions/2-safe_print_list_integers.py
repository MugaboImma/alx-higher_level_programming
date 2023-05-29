#!/usr/bin/python3
"""
A function that prints the first x elements of a list and only integer
s, it will return the real number of integers printed
"""
def safe_print_list_integers(my_list=[], x=0):
    new_list = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            new_list += 1
        except (ValueError, TypeError):
            continue
        print("")
        return(new_list)
