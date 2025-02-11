#!/usr/bin/python3
"""
Module
"""


import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self._name = name
        self._age = age
        self._is_student = is_student

    @property
    def name(self):
        """
        Getter pour l'attribut name.
        Retourne la valeur de name.
        """
        return self._name

    @name.setter
    def size(self, name):
        """
        Setter pour l'attribut name.
        Vérifie que name est une string.
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name is None:
            raise ValueError("name should be a string")
        self._name = name

    @property
    def age(self):
        """
        Getter pour l'attribut age.
        Retourne la valeur de age.
        """
        return self._age

    @age.setter
    def age(self, age):
        """
        Setter pour l'attribut age.
        Vérifie que age est un entier >= 0.
        """
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be >= 0")
        self._age = age

    @property
    def is_student(self):
        """
        Getter pour l'attribut is_student.
        Retourne la valeur de is_student.
        """
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        """
        Setter pour l'attribut is_student.
        Vérifie que is_student est un booléen.
        """
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a boolean")
        self._is_student = is_student

    def display(self):
        print(f'Name: {self._name}\nAge: {self._age}\nIs student: {self._is_student}')

    def serialize(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error during serialization: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"Error during deserialization: {e}")
            return None
