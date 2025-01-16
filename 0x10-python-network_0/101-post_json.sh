#!/bin/bash
# Sends a JSON POST request to a URL then displays the response body.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
