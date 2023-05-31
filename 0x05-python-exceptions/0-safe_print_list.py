#!/usr/bin/python3
"""
A function that prints x elements of a list.
The function will Returns the real number of elements printed
"""

def safe_print_list(my_list=[], x=0):

    new_list = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            new_list += 1
        except IndexError:
            break
    print("")
    return (new_list)
