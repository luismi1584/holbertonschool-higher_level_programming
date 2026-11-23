# Python - Serialization

This project introduces serialization and deserialization in Python.

## Task 0: Basic Serialization

File: task_00_basic_serialization.py

The module provides two functions:

- serialize_and_save_to_file(data, filename)
  Serializes a Python dictionary to a JSON file.
  Existing file contents are overwritten.

- load_and_deserialize(filename)
  Reads a JSON file and returns the deserialized dictionary.

The implementation uses Python's built-in json module,
UTF-8 encoding, and the with statement for file handling.

## Task 1: Pickling Custom Classes

File: task_01_pickle.py

This task demonstrates serialization and deserialization of
custom Python objects using the pickle module.

### CustomObject

Attributes:
- name: string
- age: integer
- is_student: boolean

Methods:
- display(): prints the object's attributes.
- serialize(filename): saves the current object to a binary file.
- deserialize(filename): reconstructs a CustomObject instance.

The implementation uses binary file modes and handles
missing or malformed files by returning None.

Important: Only unpickle files from trusted sources.
