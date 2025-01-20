#!/usr/bin/python3
"""
    this python script takes a letter and sends it to a given url
    using the POST method
"""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"

    req = requests.post(url, data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
