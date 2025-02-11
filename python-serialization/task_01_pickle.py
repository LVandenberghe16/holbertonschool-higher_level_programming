#!/usr/bin/python3
"""
Module for serializing and deserializing a custom object using pickle.
"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name  # Uses the setter method
        self.age = age
        self.is_student = is_student

    @property
    def name(self):
        """Getter for name."""
        return self._name

    @name.setter
    def name(self, name):
        """Setter for name, ensuring it is a valid string."""
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name is None or name.strip() == "":
            raise ValueError("name cannot be empty or None")
        self._name = name

    @property
    def age(self):
        """Getter for age."""
        return self._age

    @age.setter
    def age(self, age):
        """Setter for age, ensuring it is a non-negative integer."""
        if not isinstance(age, int):
            raise TypeError("age must be an integer")
        if age < 0:
            raise ValueError("age must be >= 0")
        self._age = age

    @property
    def is_student(self):
        """Getter for is_student."""
        return self._is_student

    @is_student.setter
    def is_student(self, is_student):
        """Setter for is_student, ensuring it is a boolean."""
        if not isinstance(is_student, bool):
            raise TypeError("is_student must be a boolean")
        self._is_student = is_student

    def display(self):
        """Displays the object's attributes."""
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Is Student: {self.is_student}')

    def serialize(self, filename):
        """Serializes the object to a file."""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            print(f"Error during serialization")

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file."""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError):
            print(f"Error during deserialization")
            return None
