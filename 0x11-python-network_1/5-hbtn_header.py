#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL
   and display the value of the variable X-Request-ID in
   the response header using the requests package
"""

import sys
import requests


def display_response_header_value(resource):
    """A function that take a URL, sends a request
       to the URL & displays the value of the variable
       X-Request-id
    """
    with requests.get(resource) as response:
        # print(dir(response))
        response_dict = response.headers
        print(response_dict['X-Request-Id'])


if __name__ == "__main__":
    display_response_header_value(sys.argv[1])
