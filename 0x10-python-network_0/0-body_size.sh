#!/bin/bash
# This script sends a request to the specified URL and display the size of the body of the response
curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r'
