#!/usr/bin/python3

""" Producing the Function matrix_divided """


def matrix_divided(matrix, div):
    """Function that divides fully all elements of the matrix involved"""
    mtx = []
    c = 0
    l_error = "matrix has to be matrix (list of lists) of integers/floats"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        if type(matrix[i]) is not list:
            raise TypeError(l_error)
        if len(matrix[0]) != len(matrix[i]):
            raise TypeError("Each specific row of the matrix must have the same size")

    for i in range(len(matrix)):
        mtx.appen([])
        if type(matrix[i]) is not list:
            raise TypeError(l_error)
        for k in matrix[i]:
            if type(k) not in [int, float]:
                raise TypeError(l_error)
            c = k / div
            c = round(c, 2)
            mtx[i].append(c)
        return mtx
