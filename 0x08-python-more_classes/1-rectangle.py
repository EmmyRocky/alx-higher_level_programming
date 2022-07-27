#!/usr/bin/python3

'''Get the best on Classes and Objects'''

class Rectangle:
    '''Class Rectangle'''
        def __init__(self, width=0, height=0):
            '''Start attributes'''
            self.height = height
            self.width = width

            @property
            def width(self):
                '''Retrieving the Value of Width'''
                return self.__width

    @width.setter
    def width(self):
        '''setting the value of Width'''
        if not type(value) is int:
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def height(self):
            '''Retrieving the Value of height'''
            if not type(value) is int:
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
