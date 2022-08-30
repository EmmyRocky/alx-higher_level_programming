#!/usr/bin/python3

def divivsible_by_2(my_list=[]):
    newer_list = []
    for element in my_list:
        if element % 2 == 0:
            newer_list.append(True)
        else:
            newer_list.append(False)
            return (newer_list)
