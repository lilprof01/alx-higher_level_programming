#!/usr/bin/python3
"""
    A python script that fetches a url using the urllib library methods
"""

from urllib.request import urlopen, Request

url = "https://alx-intranet.hbtn.io/status"
req = request(url)
with urlopen(req) as res:
    content = res.read()

print("Body response:")
print(f"\t- type:", type(content))
print(f"\t- content:", (content))
print(f"\t- utf8 content:", content.decode('utf-8'))
