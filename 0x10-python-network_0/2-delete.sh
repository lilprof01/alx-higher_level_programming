#!/bin/bash
# sends a DELETE request to the URL then displays the body of the response
curl -s "$1" -X DELETE
