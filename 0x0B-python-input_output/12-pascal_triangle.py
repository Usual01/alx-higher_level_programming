#!/usr/bin/python3
"""defines a Pascal's Triangle function- gives the longest side"""


def pascal_triangle(size):
    """Represents Pascal's Triangle
    """
    if size <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != size:
        shape = triangles[-1]
        tmp = [1]
        for i in range(len(shape) - 1):
            tmp.append(shape[i] + shape[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
