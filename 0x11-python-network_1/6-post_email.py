#!/usr/bin/python3
"""
    this python script sends a post request to a given url
    with a given email as parameter then displays the body of response
"""

from sys import argv
from requests import post

if __name__ == '__main__':

    url = argv[1]
    email = argv[2]

    res = post(url, {'email': email})
    print(res.text)
