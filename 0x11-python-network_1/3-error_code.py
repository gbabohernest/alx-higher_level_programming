#!/usr/bin/python3
"""This module defines a function that takes in a URL, sends a request
   to the URL and displays the body of the response(decoded in utf-8).
   Handles HTTPError exceptions and print Error code.
"""

import sys
import urllib.request
import urllib.error


def error_code(resource):
    """A function that takes a URL, send a request,
       display response decoded in utf-8, handles
       exceptions and print Error code
    """
    try:
        with urllib.request.urlopen(resource) as response:
            response_body = response.read().decode('utf-8')
            print(response_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    error_code(sys.argv[1])
