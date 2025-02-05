#!/usr/bin/python3

"""
Module
"""

class CountedIterator:
    def __init__(self, iterable):
        """Initialize with an iterable and a counter."""
        self.iterator = iter(iterable)  # Convert iterable to an iterator
        self.count = 0  # Initialize counter

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Override next to return the next item and increment the counter."""
        try:
            item = next(self.iterator)  # Fetch the next item
        except StopIteration:
            raise StopIteration  # Stop iteration when no items are left
        self.count += 1  # Increment the counter
        return item

    def get_count(self):
        """Return the number of items iterated over."""
        return self.count
