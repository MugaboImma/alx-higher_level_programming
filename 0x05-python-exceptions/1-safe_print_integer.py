#!/usr/bin/python3
"""
A function that prints an integer with "{:d}".format()
It returns True if value has been correctly printed (it means the valueis an integer) Otherwise, returns False
"""
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
