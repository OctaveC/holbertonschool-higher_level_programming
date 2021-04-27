#!/usr/bin/python3
def uppercase(str):
    for ite in str:
        ascii = ord(ite)
        if ascii > 96 and ascii < 123:
            ascii = ascii - 32
        print(chr(ascii), end="")
    print("")
