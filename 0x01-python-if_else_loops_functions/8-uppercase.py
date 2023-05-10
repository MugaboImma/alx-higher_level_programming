#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(c) >= 97 and ord(c) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end="")
    print("")
