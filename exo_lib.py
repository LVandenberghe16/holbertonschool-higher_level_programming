class Bibliotheque:
    """Defines a Bibliotheque."""

    max_authors = 5

    def __init__(self, name):
        self.name = name
        self.dict_authors = {}
        self.nb_books = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    def ajouter_auteur(self, auteur):
        if len(self.dict_authors) < self.max_authors:
            self.dict_authors[auteur] = []
        else:
            print("Impossible d'ajouter un nouvel auteur, la bibliothèque a déjà 5 auteurs")

    def ajouter_livre(self, auteur, livre):
        if auteur not in self.dict_authors and len(self.dict_authors) < self.max_authors:
            self.dict_authors[auteur] = [livre]
            self.nb_books += 1
        elif auteur in self.dict_authors:
            self.dict_authors[auteur].append(livre)
            self.nb_books += 1
        else:
            print("L'auteur n'existe pas dans la bibliothèque")

    def supprimer_livre(self, auteur, livre):
        if auteur in self.dict_authors and livre in self.dict_authors[auteur]:
            self.dict_authors[auteur].remove(livre)
            self.nb_books -= 1
        else:
            print("Le livre n'existe pas dans la bibliothèque")

    def supprimer_auteur(self, auteur):
        if auteur in self.dict_authors:
            del self.dict_authors[auteur]
        else:
            print("L'auteur n'existe pas dans la bibliothèque")

    def recuperer_livres_auteur(self, auteur):
        if auteur in self.dict_authors:
            return self.dict_authors[auteur]
        else:
            print("L'auteur n'existe pas dans la bibliothèque")

    def recuperer_livre(self, auteur, livre):
        if auteur in self.dict_authors and livre in self.dict_authors[auteur]:
            return livre
        else:
            print("Le livre n'existe pas dans la bibliothèque")
