#!/usr/bin/python3
def no_c(my_string):
    without_c = ""
    for ite in my_string:
        if (ite is not 'c') and (ite is not 'C'):
            without_c += ite
    return without_c
