#!/usr/bin/python3
"""
    This is a module that multiplies 2 matrices
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ This is a function that lazily multiplies 2 matrices """
    return np.matmul(m_a, m_b)
