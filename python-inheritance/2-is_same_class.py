#!/usr/bin/python3

"""
Module
"""


def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance a_class, otherwise False."""
    return type(obj) is a_class
