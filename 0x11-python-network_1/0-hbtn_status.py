#!/usr/bin/python3
"""This module fetches an internet resource form
   https://alx-intranet.hbtn.io/status using the
   package urllib and display the body of the response
"""
import urllib.request


def fetch_my_status():
    """This function fetches a resource
       from https://alx-intranet.hbtn.io/status
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        response_bytes = response.read()
        response_str = response_bytes.decode('utf-8')

        print("Body response:")
        print("\t- type:", type(response_bytes))
        print("\t- content:", response_bytes)
        print("\t- utf8 content:", response_str)
        # print(help(response_bytes))


if __name__ == "__main__":
    fetch_my_status()
