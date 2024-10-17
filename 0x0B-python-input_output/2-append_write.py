#!/usr/bin/python3
"""
   module contains function append_write
"""


def append_write(filename="", text=""):
    """
       appeneds string at end of file
    """
    with open(filename, mode="a") as data_file:
        return data_file.write(text)
