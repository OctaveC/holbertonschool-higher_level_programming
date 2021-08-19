#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -swo /dev/null "%{http_code}" "$1"