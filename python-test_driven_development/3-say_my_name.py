#!/usr/bin/python3
"""
This module defines a function to print a full name.

The function `say_my_name` takes two arguments (first_name and last_name),
and prints "My name is <first_name> <last_name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name (default is an empty string).

    Raises:
    TypeError: If first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter", "White")
    My name is Walter White
    >>> say_my_name("Bob")
    My name is Bob
    >>> say_my_name(12, "White")
    TypeError: first_name must be a string
    """

    if type(first_name) not in [str]:
        raise TypeError("first_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
