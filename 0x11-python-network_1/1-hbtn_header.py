#!/usr/bin/python3
"""This module takes in a URL, sends a request to the URL
   and display the value of the X-Request-ID
"""

import sys
import urllib.request


def response_header_value(resource):
    """A function that take a URL, sends a request
    to the URL & displays the value of the X-Request-id
    """
    with urllib.request.urlopen(resource) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    response_header_value(url)
