#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix

    Arg:
        matrix: 2d list of integers

    Returns:
        New matrix with corresponding items of matrix argument squared
    '''
    squared = []
    for arr in matrix:
        squared.append(list(map(lambda x: x**2, arr)))
    return squared
