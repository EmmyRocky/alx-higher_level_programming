#!/usr/bin/python3
""" Square class to identify that this is a square """


class Square():
    """ square class describing the size & proper validation """

    def __init__(self, size=0, position=(0, 0)):
        """ Start up data """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrieving the size """
        return self.__size

    @property
    def position(self):
        """ retrieving the position """
        return self.__position

    @size.setter
    def size(self, value):
        """ determine size """
        if (type(value) is not int):
            raise TypeError("size must be an int")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """ determine position """
        if (type(value) is not tuple):
            raise TypeError
        elif (len(value) is not 2):
            raise TypeError
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError
        else:
            self.__position = value

    def area(self):
        """ retrieve area of the square """
        return self.size ** 2

    def my_print(self):
        """ print the square """
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
