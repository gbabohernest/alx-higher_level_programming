#!/bin/bash
# This script sends a request to the specified URL and displays only the status code of the response
curl -sI "$1"  -w '%{http_code}\n'
