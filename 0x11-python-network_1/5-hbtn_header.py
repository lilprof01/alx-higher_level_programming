#!/usr/bin/python3
"""
    this python script takes in a url as argument
    and sends a request to the url then displays the X-Request-Id
    in response header
"""

from sys import argv
from requests import get

if __name__ == "__main__":
    url = argv[1]
    print(get(url).headers.get('X-Request-Id'))
