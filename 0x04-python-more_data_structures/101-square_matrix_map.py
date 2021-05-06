#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda ite: list(map(lambda ite2: ite2 ** 2, ite)), matrix))
