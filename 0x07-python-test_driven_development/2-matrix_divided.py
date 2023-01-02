#!/usr/bin/python3
'''matrix_divided function divides all elements of a matrix

check_dim function checks the dimension of a list has

'''


def check_dim(matrix, dim=0):
    '''Checks the dimension of a list

    Args:
        matrix: list to check its dimension
        dim: dimension of the list. Defaults to 0

    Return:
        -1 if matrix is not a list or the dimension if matrix is a list
    '''
    if isinstance(matrix, list):
        if matrix == []:
            return dim
        dim = dim + 1
        dim = check_dim(matrix[0], dim)
        return dim
    else:
        if dim == 0:
            return -1
        return dim


def matrix_divided(matrix, div):
    '''Divides all elements of a matrix

    Args:
        matrix: 2-dimensional list of integers or floats
        div: a number not equal to 0 to divide each element of the matrix

    Returns:
        New matrix with each element the result after division by div

    Raises:
        TypeError: if any element of matrix is neither float nor int
        TypeError: if matrix rows have different sizes
        TypeError: if div not a number
        ZeroDivisionError: if div is 0
    '''
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    message = 'matrix must be a matrix (list of lists) of integers/floats'

    if check_dim(matrix) != 2:
        raise TypeError(message)

    if matrix[0] == [] or matrix[1] == []:
        raise TypeError(message)

    for row in matrix:
        for e in row:
            if type(e) not in (int, float):
                raise TypeError(message)

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')

    return [[round(e/div, 2) for e in row] for row in matrix]
