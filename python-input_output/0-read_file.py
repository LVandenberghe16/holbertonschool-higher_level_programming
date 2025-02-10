#!/usr/bin/python3
"""
Module
"""


def read_file(filename=""):
    """
    méthode pour lire un fichier et le print
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
