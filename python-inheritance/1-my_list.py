#!/usr/bin/python3
"""
Module
"""


class MyList(list):
    """Custom list class that extends the built-in list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
