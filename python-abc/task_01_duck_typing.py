#!/usr/bin/python3

"""
Module
"""

from abc import ABC, abstractmethod

class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list".format(item))
        super().append(item)

    def pop(self, item):
        print("Removed [{}] from the list".format(item))
        super().pop(item)

    def extend(self, item):
        print("Extended the list with [{}]".format(item))
        super().extend(item)

    def remove(self, item):
        print("Removed [{}] from the list".format(item))
        return super().remove(item)
