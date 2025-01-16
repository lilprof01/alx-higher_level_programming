#!/bin/bash
#takes a URL and sends a GET request then displays the body of the response
curl "$1" -sH "X-School-User-Id: 98"
