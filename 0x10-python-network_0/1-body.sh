#!/bin/bash
# takes a URL and sends a GET request then displays the body of the response
curl -sfL "$1" -X GET
