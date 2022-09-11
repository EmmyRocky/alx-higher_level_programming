#!/usr/bin/python3
def search_replace(my_list, search, replace):
    dup_list = my_list.copy()
    for u in range(len(dup_list)):
        dup_list[u] = replace if my_list[u] == search else my_list[u]
    return (dup_list)
