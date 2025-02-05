#!/usr/bin/python3

"""
Module
"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass

class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return pi * self.__radius ** 2

    def perimeter(self):
        return 2 * pi * self.__radius

class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """Prints the area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
