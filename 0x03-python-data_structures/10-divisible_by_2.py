#!/usr/bin/python3

def divivsible_by_2(my_list=[]):
    new_list = list(my_list)

    for r in range(len(my_list)):
        if my_list[r] % 2 == 0:
            new_list[r] = True
        else:
            new_list[r] = False
    return new_list[r]
