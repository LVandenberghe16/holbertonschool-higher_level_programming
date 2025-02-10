#!/usr/bin/python3
"""
Module de json
"""

class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation of a Student instance with filter"""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
