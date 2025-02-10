#!/usr/bin/python3
"""
Module
"""


def write_file(filename="", text=""):
    """
    méthode pour écrire dans un fichier
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
