#!/bin/bash
# This script sends a request to the specified URL and displays only the status code of the response
curl -s -o >(grep -oP '(?<=HTTP/1\.1 )[0-9]+' | head -n1) "$1"
