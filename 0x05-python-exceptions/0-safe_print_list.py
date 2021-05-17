#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for ite in range(x):
            print(my_list[ite], end="")
    except IndexError:
        print()
        return ite
    print()
    return x
