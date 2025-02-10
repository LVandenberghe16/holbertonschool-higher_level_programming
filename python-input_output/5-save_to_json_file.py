#!/usr/bin/python3
"""
Module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    méthode pour ajouter du texte dans un fichier
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
