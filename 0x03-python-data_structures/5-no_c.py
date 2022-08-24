#!/usr/bin/python3
def no_c(my_string):
    """ Excluding all C's and c's and returning a new string """
    new_string = my_string.translate({ord(i): None for i in 'cC})
    return (new_string)
