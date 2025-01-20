#!/usr/bin/python3
"""
    This python script takes a url as argument and sends a requst to it
    and then displays the X-Request-id from the header of theh response
"""
from sys import argv
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = argv[1]

    request = Request(url)
    with urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
