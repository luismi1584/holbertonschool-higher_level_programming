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
