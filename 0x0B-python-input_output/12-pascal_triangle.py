#!/usr/bin/python3
""" Module for pascal_triangle """


def pascal_triangle(n):
    """ Returns a list of lists of integers representing """
    """ the Pascal’s triangle of n. """
    tmp = []
    total = []
    if n <= 0:
        return []
    for ite in range(n):
        ligne = []
        for ite2 in range(ite + 1):
            if (ite != 0) and (ite2 != 0) and (ite != ite2):
                ligne.append(tmp[ite2] + tmp[ite2 - 1])
            else:
                ligne.append(1)
        tmp = ligne
        total.append(ligne)
    return total
