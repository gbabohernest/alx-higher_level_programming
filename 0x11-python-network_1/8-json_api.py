#!/usr/bin/python3
"""This module defines a function that takes in a letter and
   sends a POST request to http://0.0.0.0:5000/search_user with
   the letter as a parameter.
   Displays the id and name if the response body is properly JSON
   formatted and not empty. Otherwise, displays appropriate messages.
"""

import sys
import requests


def search_api(letter=""):
    """Sends a POST request to a URL with a letter as a parameter,
          displays [<id>] <name> if the response body is properly JSON
          formatted and not empty. Otherwise, displays appropriate messages.
    """
    url = 'http://0.0.0.0:5000/search_user'
    q = {'q': letter}

    try:
        with requests.post(url, data=q) as response:
            res_dict = response.json()
            if res_dict:
                print("[{}] {}".format(res_dict['id'], res_dict['name']))
            else:
                print("No result" if not response.text else "Not a valid JSON")
    except requests.exceptions.InvalidJSONError as err:
        print("Not a valid JSON")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else ""
    search_api(arg)
