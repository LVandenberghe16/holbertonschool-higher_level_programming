#!/usr/bin/python3
def max_integer(my_list=[]):
    m = my_list[0]
    if not my_list:
        return None
    for i in range (1, len(my_list)):
        if my_list[i] > m:
            m = my_list[i]
    return m
