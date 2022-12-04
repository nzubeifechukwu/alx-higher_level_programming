#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    '''prints a matrix of integers

    Args:
        matrix: 2-d list of lists
    '''
    # mat_elements = [row[i] for row in matrix for i in len(row)]
    mat_elems = [n for row in matrix for n in row]
    for row in matrix:
        for i in range(len(row)):
            if i < len(row) - 1:
                print('{:d}'.format(row[i]), end=' ')
            else:
                print('{:d}'.format(row[i]), end='')
        print()
