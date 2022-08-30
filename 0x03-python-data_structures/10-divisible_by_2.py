#!/usr/bin/python3

def divivsible_by_2(my_list=[]):
    realbranded_list = list(my_list)

    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            realbranded_list[i] = True
        else:
            realbranded_list[i] = False
    return realbranded_list[i]
