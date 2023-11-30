#!/bin/bash
# This script sends a DELETE request to the URL passed as the first arg & display the body of the response
curl -s -X DELETE "$1"
