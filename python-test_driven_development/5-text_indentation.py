#!/usr/bin/python3
"""
This module defines a function to print text with specific formatting.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Parameters:
    text (str): The text to format and print.

    Raises:
    TypeError: If text is not a string.

    Example:
    >>> text_indentation("Hello. How are you? Fine:")
    Hello.

    How are you?

    Fine:
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False
    for char in text:
        if char in ".:?":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False
    print(result.strip(), end="")
