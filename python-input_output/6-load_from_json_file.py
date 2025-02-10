#!/usr/bin/python3
"""
Module
"""


import json


def load_from_json_file(filename):
    """
    méthode pour ajouter du texte dans un fichier
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return json.loads(file)
