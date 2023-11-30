#!/bin/bash
# This script sends a GET request to the specified URL & displays the body for a 200 status code
curl -s -w "\n%{http_code}\n" "%1" | awk '/^200$/ {p=1; next} p'
