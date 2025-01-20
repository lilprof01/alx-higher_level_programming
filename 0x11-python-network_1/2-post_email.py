#!/usr/bin/python3
"""
    this python script takes a url and email as argument
    and sends a post request to the url with the mail as param
    then displays the body of response in decoded utf-8
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
