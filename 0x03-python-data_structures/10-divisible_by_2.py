#!/usr/bin/python3

# A function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    multiple_of_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiple_of_2.append(True)
        else:
            multiple_of_2.append(False)

    return (multiple_of_2)
