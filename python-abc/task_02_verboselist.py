#!/usr/bin/python3

"""
Module
"""

class VerboseList(list):
    def append(self, item):
        print("Added [{}] to the list".format(item))
        super().append(item)

    def pop(self, item):
        super().pop(item)
        print("Removed [{}] from the list".format(item))
        return item

    def extend(self, item):
        print("Extended the list with [{}]".format(len(item)))
        super().extend(item)

    def remove(self, item):
        print("Removed [{}] from the list".format(item))
        return super().remove(item)
