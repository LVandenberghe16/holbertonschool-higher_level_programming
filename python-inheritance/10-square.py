#!/usr/bin/python3

"""
Module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initializes a square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
