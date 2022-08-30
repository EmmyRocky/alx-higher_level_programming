#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    brandedrelease_list = list(my_list)
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            brandedrelease_list[i] = True
        else:
            brandedrelease_list[i] = False
    return brandedrelease_list
