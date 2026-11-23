#!/usr/bin/env python3
"""Convert CSV data into JSON format."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file into data.json and return success status."""
    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True
    except (OSError, csv.Error, UnicodeError, TypeError, ValueError):
        return False
