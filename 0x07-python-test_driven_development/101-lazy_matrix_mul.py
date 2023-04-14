#!/usr/bin/python3

"""This module performs multiplication operation on two modules"""

import numpy as matrix_mul


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Arguments:
        m_a (list of lists of ints/floats): The first matrix., m_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(m_a, m_b))
