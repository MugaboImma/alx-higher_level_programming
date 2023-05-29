#!/usr/bin/python3
"""
Python function def magic_calculation(a, b): that does the Python bytecode
"""
def magic_calculation(a, b):
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                res += a **b / i
        except:
            res = b + a
            break
    return (res)
