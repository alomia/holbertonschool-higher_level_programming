#!/usr/bin/python3
import json
"""returns an object (Python data structure)represented by a JSON string
"""


def from_json_string(my_str):
    """object python convert to JSON
    """
    return json.loads(my_str)
