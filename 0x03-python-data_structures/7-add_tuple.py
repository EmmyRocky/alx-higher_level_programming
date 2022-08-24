#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """ tuples are being added up all together """
    if len(tuple_a) >= 2:
        first_tup_0 = tuple_a[0]
        first_tup_1 = tuple_a[1]
    if len(tuple_b) >= 2:
        second_tup_0 = tuple_b[0]
        second_tup_1 = tuple_b[1]
    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            first_tup_1 = 0
            first_tup_0 = tuple_a[0]
        else:
            first_tup_1, first_tup_0 = (0, 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            second_tup_1 = 0
            second_tup_0 = tuple_b[0]
        else:
            second_tup_0, second_tup_1 = (0, 0)
    new_tuple = (first_tup_0 + second_tup_0, first_tup_1 + second_tup_1)
    return (new_tuple)
