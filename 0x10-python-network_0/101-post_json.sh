#!/bin/bash
# This script sends a JSON POST request to the specified URL with the contents of a file in the body
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
