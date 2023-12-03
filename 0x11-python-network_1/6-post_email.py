#!/usr/bin/python3
"""This module take in a URL and an email, sends a POST
   request to the passed URL with the email as param and
   displays the body of the response using the request package
"""

import sys
import requests


def post_an_email(resource, email_address):
    """A function that sends a POST request to the
       URL with email as param and display the body
       of the response using the requests package
    """
    data = {'email': email_address}
    with requests.post(resource, data=data) as response:
        response_dict = response.json()
        print(response_dict.get('text'))


if __name__ == "__main__":
    post_an_email(sys.argv[1], sys.argv[2])
