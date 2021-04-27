#!/usr/bin/python3
for ite in range(90, 64, -1):
    if ite % 2 == 0:
        print("{}".format(chr(ite + 32)), end="")
    else:
        print("{}".format(chr(ite)), end="")
