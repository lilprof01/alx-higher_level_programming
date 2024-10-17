#!/usr/bin/python3
"""
   module contains function from_json_string
"""


import json


def from_json_string(my_str):
    """
       returns an object represented by a JSON
    """
    return json.loads(my_str)
