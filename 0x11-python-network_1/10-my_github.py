#!/usr/bin/python3
"""
    this python script takes github credentials as argument
    and displays user id using the github api
"""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    auth = HTTPBasicAuth(username, password)
    res = get("https://api.github.com/user", auth=auth)
    print(res.json().get('id'))
