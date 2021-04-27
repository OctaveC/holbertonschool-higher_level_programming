#!/usr/bin/python3
for ite in range(0, 100):
    if ite != 99:
        print("{:0>2d}".format(ite), end=", ")
    else:
        print(ite)
