#!/usr/bin/python3

"""
A program that imports all functions from
the file calculator_1.py and handles basic operations.
"""
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    oper = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div
            }
    if argv[2] in oper:
        num_1 = int(argv[1])
        num_2 = int(argv[3])
        op = oper[argv[2]]
        res = op(num_1, num_2)
        print('{:d} {:s} {:d} = {:d}'.format(num_1, argv[2], num_2, res))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
