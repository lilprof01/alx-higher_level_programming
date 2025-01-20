#!/usr/bin/python3
"""
    this python script sends a request to a given url
    handles Error and then displays the body of the response
"""
from sys import argv
from requests import get

if __name__ == "__main__":
    req = get(argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(req.text)
