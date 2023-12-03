#!/usr/bin/python3
"""This module defines a function that takes your GitHub
   credentials(username, password) & uses the GitHub API
   to display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth as Basic_auth


def get_my_github_id(username, password):
    """
        Retrieves the GitHub user id using the GitHub API
        with basic authentication.
        :param username: GitHub username
        :param password: GitHub password or personal access token
    """
    url = 'https://api.github.com/user'
    try:
        with requests.get(url, auth=Basic_auth(
                username, password)) as response:
            res_json = response.json()
            print(res_json['id'])
    except Exception as e:
        print("None")


if __name__ == "__main__":
    get_my_github_id(sys.argv[1], sys.argv[2])
