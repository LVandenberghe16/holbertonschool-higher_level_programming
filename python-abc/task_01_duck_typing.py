#!/usr/bin/python3

"""
Module
"""


class VerboseList(list):
    """Classe qui étend list en affichant des messages pour certaines opérations."""

    def append(self, item):
        """Ajoute un élément à la liste avec un message."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Ajoute plusieurs éléments à la liste avec un message."""
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Supprime un élément de la liste avec un message."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Retire et retourne un élément de la liste avec un message."""
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item