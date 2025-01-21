#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dic = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dic.items():
        print("{}: {}".format(key, value))
