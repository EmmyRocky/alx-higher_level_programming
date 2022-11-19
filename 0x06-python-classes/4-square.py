#!/usr/bin/python3
""" We are exploring more about class """


class Square():
    """ square class describing the size & proper validation """

    def __init__(self, size=0):
        """ Here Initilizes the data """
        self.__size = size

    @property
    def size(self):
        """ Here draws in the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size to a value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Sends back the current square area """
        return self.__size ** 2
