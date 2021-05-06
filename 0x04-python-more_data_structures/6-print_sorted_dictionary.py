#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for ite in sorted(a_dictionary):
        print("{}: {}".format(ite, a_dictionary[ite]))
