#!/usr/bin/python3
"""
    this python script takes a url as argument
    sends a request to the url and displays the body of
    response in a decoded utf-8 format
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    try:
        url = argv[1]
        with urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
