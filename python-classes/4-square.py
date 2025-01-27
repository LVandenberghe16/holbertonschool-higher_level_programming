#!/usr/bin/python3
"""
Ce module définit une classe square (ou carré)
"""


class Square:
    """
    Cette classe représente un carré
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """
        Getter pour l'attribut __size.
        Retourne la valeur de __size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut __size.
        Vérifie que value est un entier >= 0 avant de l'affecter.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
