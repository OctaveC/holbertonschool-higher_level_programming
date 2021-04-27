#!/usr/bin/python3
for ite1 in range(0, 10):
    for ite2 in range(ite1 + 1, 10):
        if ite1 != 8:
            print("{}{}".format(ite1, ite2), end=", ")
        else:
            print("{}{}".format(ite1, ite2))
