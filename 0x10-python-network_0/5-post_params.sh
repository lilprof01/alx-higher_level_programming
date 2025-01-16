#!/bin/bash
#  takes a URL, sends a POST request, then displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
