#!/usr/bin/python3

# A function that returns the weighted average of all
# integers tuple (<score>, <weight>)
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = 0
    d = 0

    for int_tuple in my_list:
        n += int_tuple[0] * int_tuple[1]
        d += int_tuple[1]

    return (n / d)
