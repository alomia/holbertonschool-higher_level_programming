#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix is None:
        return None
    for i in matrix:
        new_matrix.append([j ** 2 for j in i])
    return new_matrix
