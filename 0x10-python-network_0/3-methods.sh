#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep "Allow:" | sed "s|Allow: ||"
