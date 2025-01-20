#!/usr/bin/python3
def print_list_integer(my_list=[]):
    size = len(my_list)
    i = 0
    for i in range (size):
        print("{}\n".format(my_list[i]), end="")

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)