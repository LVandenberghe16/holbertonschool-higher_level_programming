#!/usr/bin/python3
import sys

argc = len(sys.argv)
for i in range(argc):
    print("{}: {}".format(i, sys.argv[i]))