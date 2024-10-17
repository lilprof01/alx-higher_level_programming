#!/usr/bin/python3
"""
   module contains function to_json_string
"""


import json


def to_json_string(my_obj):
    """
       json representation of object
    """
    return json.dumps(my_obj)
