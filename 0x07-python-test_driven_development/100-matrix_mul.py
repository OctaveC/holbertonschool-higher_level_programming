#!/usr/bin/python3
"""
    This is a module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """ This is a function that multiplies 2 matrices """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for ite in m_a:
        if type(ite) is not list:
            raise TypeError("m_a must be a list of lists")
    for ite in m_b:
        if type(ite) is not list:
            raise TypeError("m_b must be a list of lists")

    if len(m_a) is 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) is 0:
        raise ValueError("m_b can't be empty")

    for ite in m_a:
        if len(ite) is 0:
            raise ValueError("m_a can't be empty")
    for ite in m_b:
        if len(ite) is 0:
            raise ValueError("m_b can't be empty")

    for ite in m_a:
        for col in ite:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for ite in m_b:
        for col in ite:
            if type(col) is not int and type(col) is not float:
                raise TypeError("m_b should contain only integers or floats")

    for ite in m_a:
        if len(ite) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for ite in m_b:
        if len(ite) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for ite1 in range(len(m_a)):
        new_row = []
        for ite2 in range(len(m_b[0])):
            product = 0
            for ite3 in range(len(m_a[0])):
                product += m_a[ite1][ite3] * m_b[ite3][ite2]
            new_row.append(product)
        new_matrix.append(new_row)
    return new_matrix
