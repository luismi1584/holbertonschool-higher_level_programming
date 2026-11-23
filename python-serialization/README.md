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

## Task 2: Converting CSV Data to JSON

File: task_02_csv.py

The convert_csv_to_json(csv_filename) function reads a CSV file
using csv.DictReader and writes the records to data.json.

The function:
- Converts CSV rows into a list of dictionaries.
- Uses json.dump() to serialize the data.
- Returns True when conversion succeeds.
- Returns False when the input cannot be processed.
- Preserves CSV field values as strings.

Example:

    convert_csv_to_json("data.csv")

Output file:

    data.json

## Task 3: Serializing and Deserializing with XML

File: task_03_xml.py

This task demonstrates XML serialization and deserialization
using Python's xml.etree.ElementTree module.

Functions:
- serialize_to_xml(dictionary, filename):
  Converts a dictionary into an XML document and saves it.

- deserialize_from_xml(filename):
  Reads an XML document and reconstructs a Python dictionary.

The XML document uses a data root element and child elements
for each dictionary key.

Values are serialized as text, so deserialized values are
strings rather than their original Python numeric or boolean types.
