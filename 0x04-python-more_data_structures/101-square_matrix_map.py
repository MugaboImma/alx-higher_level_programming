#!/usr/bin/python3

# A function that computes the square value of all integers
# of a matrix using map
def square_matrix_map(matrix=[]):
    return (list(map(lambda a: list(map(lambda b: b ** 2, a)), matrix)))
