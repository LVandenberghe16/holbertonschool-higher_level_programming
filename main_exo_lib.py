#!/usr/bin/python3
from exo_lib import Library
from comic_library import ComicLibrary

def main():
    # Create a library
    print("=== Creating Library ===")
    my_library = Library("City Library")
    print(my_library)

    # Test setters
    print("\n=== Testing modifications ===")
    my_library.name = "Grand Library"

    # Add authors and books
    print("\n=== Adding authors and books ===")
    my_library.add_author("William Shakespeare")
    my_library.add_book("William Shakespeare", "Romeo and Juliet")
    my_library.add_book("William Shakespeare", "Hamlet")
    print(my_library.authors)  # Print authors dictionary

    # Display books by author
    print("\n=== List of books by author ===")
    books = my_library.get_books_by_author("William Shakespeare")
    print(books)

    # Test book search
    print("\n=== Book search ===")
    book = my_library.get_book("William Shakespeare", "Hamlet")
    print(book)

    # Test deletion
    print("\n=== Testing deletion ===")
    my_library.delete_book("William Shakespeare", "Romeo and Juliet")
    my_library.get_books_by_author("William Shakespeare")

    # Test errors
    print("\n=== Testing errors ===")
    try:
        my_library.add_author("William Shakespeare")  # Author already exists
    except KeyError as e:
        print(f"Expected error: {e}")

    try:
        my_library.get_books_by_author("Jane Austen")  # Author doesn't exist
    except KeyError as e:
        print(f"Expected error: {e}")

    # Création d'une bibliothèque de BD
    comic_lib = ComicLibrary("Ma Bibliothèque de BD")

    # Ajout de BD
    comic_lib.add_book("Hergé", "Tintin au Tibet", "Tintin")
    comic_lib.add_book("Hergé", "Le Lotus Bleu", "Tintin")

    # Recherche par série
    tintin_books = comic_lib.get_comics_by_serie("Tintin")
    print(tintin_books)


    # Recherche d'artiste
    title = comic_lib.get_comic("Hergé", "Le Lotus Bleu")
    print(title)

if __name__ == "__main__":
    main()
