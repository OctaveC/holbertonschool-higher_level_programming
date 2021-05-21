#!/usr/bin/python3
"""
    This is a module that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in matrix:
        if type(row) is not list or len(row) is 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for column in row:
            if type(column) is not int and type(column) is not float:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return [[round(ite2 / div, 2) for ite2 in ite1] for ite1 in matrix]
