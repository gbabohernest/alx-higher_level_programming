#!/usr/bin/python3
"""This module defines a function that takes in a URL,
   sends a request to the URL and displays the body of
   the response, and display Error code if HTTP status
   code is greater than or equal to 400.
   <Error code> <status code>
"""

import sys
import requests


def display_http_error_code(resource):
    """Sends a request to a URL, display the body
       of the response, and display <Error code>
       <status code> if HTTP status code is >= 400
    """
    try:
        with requests.get(resource) as response:
            response.raise_for_status()
            print(response.text)
    except requests.exceptions.HTTPError as err:
        print("Error code: {}".format(err.response.status_code))


if __name__ == "__main__":
    display_http_error_code(sys.argv[1])
