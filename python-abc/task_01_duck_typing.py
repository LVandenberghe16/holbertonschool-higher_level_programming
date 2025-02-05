#!/usr/bin/python3

"""
Module
"""

from abc import ABC, abstractmethod

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def pop(self, item):
        super().pop(item)
        print("Removed [{}] from the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}]".format(item))

    def remove(self, item):
        return super().remove(item)
        print("Removed [{}] from the list".format(item))
