
#!/usr/bin/env python3
"""Serialize and deserialize custom Python objects using pickle."""

import pickle


class CustomObject:
    """Represent an object with personal attributes."""

    def __init__(self, name, age, is_student):
        """Initialize the object's attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize this instance to a binary file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a binary file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if isinstance(obj, cls):
                return obj
        except (OSError, pickle.UnpicklingError, EOFError,
                AttributeError, ImportError):
            return None
        return None
