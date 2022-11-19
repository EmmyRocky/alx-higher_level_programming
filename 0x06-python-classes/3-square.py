#!/usr/bin/python3
""" This is where the class square defines a square """


class Square():
    """ square class describing the size & proper validation """

    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an interger")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
