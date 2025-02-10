#!/usr/bin/python3

def read_file(filename=""):
    f = open(filename, 'r', encoding="utf-8")
    print(f.read(), end="")
