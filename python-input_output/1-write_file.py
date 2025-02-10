#!/usr/bin/python3

def read_file(filename=""):
    f = open(filename, 'r')
    print(f.read(), end="")


read_file("my_file_0.txt")