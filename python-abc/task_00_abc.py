#!/usr/bin/python3

"""
Module
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """An abstract class representing an animal."""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """A class representing a dog."""
    def sound(self):
        return "Bark"

class Cat(Animal):
    """A class representing a cat."""
    def sound(self):
        return "Meow"
