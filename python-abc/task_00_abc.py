#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    """An abstract class representing an animal."""
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    """A class representing a dog."""
    def sound(self):
        print("Bark")

class Cat(Animal):
    """A class representing a cat."""
    def sound(self):
        print("Meow")
