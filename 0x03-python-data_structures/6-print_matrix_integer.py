#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ro in matrix:
        for col in matrix:
            print("{:d}".format(col), end="" if col != ro[-1] else "")
        print()
