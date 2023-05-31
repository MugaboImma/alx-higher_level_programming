#!/usr/bin/python3
for dig_1 in range(0, 9):
    for dig_2 in range(dig_1 + 1, 10):
        if dig_1 != 8 or dig_2 != 9:
            print("{:d}{:d}".format(dig_1, dig_2), end=", ")
        else:
            print("{:d}{:d}".format(dig_1, dig_2))
