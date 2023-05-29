#!/usr/bin/python3
import sys

"""
A function that executes a function safely
Returns the result of the function,
Otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:
"""
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
