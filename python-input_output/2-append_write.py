#!/usr/bin/python3
"""
Module
"""


def append_write(filename="", text=""):
    """
    méthode pour ajouter du texte dans un fichier
    """
    with open(filename, 'w', encoding="utf-8") as f:
        f.append(text)
        return len(text)
