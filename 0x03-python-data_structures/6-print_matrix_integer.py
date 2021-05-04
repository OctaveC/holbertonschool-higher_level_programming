#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columns in matrix:
        padding = ""
        for ite in columns:
            print("{:s}{:d}".format(padding, ite), end='')
            padding = " "
        print("")
