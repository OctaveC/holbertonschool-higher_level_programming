#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" -X OPTIONS | grep "Allow:" | sed 'Allow: ||'
