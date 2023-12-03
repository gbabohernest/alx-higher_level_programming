#!/usr/bin/python3
"""This module take in a URL and an email, sends a POST
   request to the passed URL with the email as param and
   displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request as request
import urllib.parse


def post_an_email(resource, email_address):
    """A function that sends a POST request to the
       URL with email as param and display the body
       of the response (decoded in utf-8)
    """
    data = urllib.parse.urlencode({'email': email_address})
    data = data.encode('utf-8')
    with request.urlopen(resource, data=data) as response:
        response_body = response.read().decode('utf-8')
        # print(help(response_body))
        # print("Your email is: {}".format(response_body))
        print(response_body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_an_email(url, email)
