#!/usr/bin/python3
"""
This module defines a function to add two integers.

The function `add_integer` takes two arguments (a and b),
and returns their sum, casting any floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, returning the result as an integer.

    Parameters:
    a (int, float): The first number.
    b (int, float, optional): The second number (default is 98).

    Returns:
    int: The sum of the two numbers.

    Raises:
    TypeError: If a or b is not an integer or float.

    Example:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100.5, 2)
    102
    >>> add_integer(2)
    100
    """
    if type(a) not in [int, float] or a == "nan":
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or b == "nan":
        raise TypeError("b must be an integer")
    return int(a) + int(b)
