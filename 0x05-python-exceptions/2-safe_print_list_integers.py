#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for ite in range(x):
        try:
            print("{:d}".format(my_list[ite]), end="")
            count += 1
        except(ValueError, TypeError):
            continue;
    print()
    return count
