#!/usr/bin/python3
for ite in range(97, 123):
    if ite == 101 or ite == 113:
        continue
    print("{}".format(chr(ite)), end="")
