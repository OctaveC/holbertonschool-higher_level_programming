#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""


def find_peak(l_o_i):
    """
    Finds a peak in a list of unsorted integers.
    l_o_i stands for list_of_integers
    """
    if l_o_i == []:
        return None
    elif len(l_o_i) == 1:
        return l_o_i[0]
    elif l_o_i[0] >= l_o_i[1]:
        return l_o_i[0]
    elif l_o_i[len(l_o_i) - 1] >= l_o_i[len(l_o_i) - 2]:
        return l_o_i[len(l_o_i) - 1]

    for ite in range(1, len(l_o_i) - 1):
        if l_o_i[ite] >= l_o_i[ite + 1] and l_o_i[ite] >= l_o_i[ite - 1]:
            return l_o_i[ite]
