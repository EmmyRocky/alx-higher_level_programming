#!/usr/bin/python3
""" This holds the class Square that describes a square """


class Square():
    """ this holds the square class: size & proper validation """

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
