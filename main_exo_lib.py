#!/usr/bin/python3
from exo_lib import Bibliotheque

# Création d'une bibliothèque avec un nom et une limite de 5 auteurs
biblio = Bibliotheque("Médiathèque Centrale")

# Ajout d'auteurs et de livres
biblio.ajouter_livre("J.K. Rowling", "Harry Potter à l'École des Sorciers")
biblio.ajouter_livre("J.K. Rowling", "Harry Potter et la Chambre des Secrets")
biblio.ajouter_livre("George Orwell", "1984")
biblio.ajouter_livre("Victor Hugo", "Les Misérables")
biblio.ajouter_livre("J.R.R. Tolkien", "Le Seigneur des Anneaux")

# Tentative d'ajout d'un 6e auteur (devrait échouer)
biblio.ajouter_livre("Albert Camus", "L'Étranger")  # Impossible car la bibliothèque a déjà 5 auteurs

# Récupération des livres d'un auteur
print("📚 Livres de J.K. Rowling :", biblio.recuperer_livres_auteur("J.K. Rowling"))

# Suppression d'un livre
biblio.supprimer_livre("George Orwell", "1984")

# Récupération d'un livre spécifique
print("📖 Recherche d'un livre :", biblio.recuperer_livre("J.K. Rowling", "Harry Potter et la Chambre des Secrets"))

# Suppression d'un auteur entier
biblio.supprimer_auteur("Victor Hugo")

# Vérification de l'état final des auteurs et livres
print("📚 État final des auteurs :", biblio.dict_authors)