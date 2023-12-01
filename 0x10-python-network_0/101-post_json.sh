#!/bin/bash
# This script sends a JSON POST request to the specified URL with the contents of a file in the body
curl -sF "data=$2" "$1"
