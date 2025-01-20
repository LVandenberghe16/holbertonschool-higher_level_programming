#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([pow(x, 2) for x in row])
    return new_matrix
