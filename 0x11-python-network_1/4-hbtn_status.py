#!/usr/bin/python3
"""
    this python script fetches a given url
"""
from requests import get

if __name__ == '__main__':
    res = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(res.text)}')
    print(f'\t- content: {res.text}')
