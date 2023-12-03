#!/usr/bin/python3
"""This module fetches data from https://alx-intranet.hbtn.io/status
   using the requests package and display type and content of the response
"""

import requests


def what_is_my_status():
    """This function fetches data from
       https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as response:
        response_body = response.text
        response_str = response.encoding
        print("Body response:")
        print("\t- type: {}".format(type(response_str)))
        print("\t- content: {}".format(response_body))


if __name__ == "__main__":
    what_is_my_status()
