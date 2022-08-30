#!/usr/bin/python3

def divivsible_by_2(my_list=[]):
    realbranded_list = list(my_list)

    for r in range(len(my_list)):
        if my_list[r] % 2 == 0:
            realbranded_list[r] = True
        else:
            realbranded_list[r] = False
    return realbranded_list[r]
