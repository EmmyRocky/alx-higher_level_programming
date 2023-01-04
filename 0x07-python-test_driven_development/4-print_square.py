#!/usr/bin/python3

""" Producing the Function print_square """


def print_square(size):
    if type(size) not in [int]:
        raise TypeError("size has to an integer")
    if size < 0:
        raise ValueError("size has to be >= 0")
    if type(size) in [float] and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
