#!/usr/bin/python3

"""Bringing into existence the Function add_integer"""


def add_integer(a, b=98):
    """The Function that will add 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
