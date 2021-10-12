#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: object python convert JSON
        filename: file create
    """
    with open(filename, 'w', encoding="utf-8") as w:
        w.write(json.dumps(my_obj))
