#!/usr/bin/python3
'''
    this module contains matrix_divided
    the function divides a matrix and returns a new matrix
    args:
        matrix - the matrix to be divided
        div - the divider(an integer or float)
'''


def matrix_divided(matrix, div):
    '''
    this function divides a matrix
    Matrix must be a list of integers or floats, otherwise
    will raise a TypeError.
    Each row must be the same size, otherwise will raise
    a TypeError.
    Div must be a number, otherwise, raise a TypeError.
    Div can't be zero, otherwise, ZeroDivisionError.
    All elements will be divided by div and rounded to 2 decimal places.
    Returns new matrix.
    '''

    new_matrix = []
    length = 0

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or len(matrix[0]) == 0 \
            or len(matrix) <= 0:
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        length = len(matrix[0])
        if len(i) is not length:
            raise TypeError('Each row of the matrix must have the same size')
        new_row = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
            k = round(j / div, 2)
            new_row.append(k)
        new_matrix.append(new_row)
    return new_matrix
