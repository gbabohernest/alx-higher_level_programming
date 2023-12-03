#!/usr/bin/python3
"""A script that list 10 commits(from most recent to oldest)
   of the repo 'rails' by the user 'rails' using GitHub API
"""

import sys
import requests
from requests.auth import HTTPBasicAuth as Basic_auth


def list_commits(repo, owner):
    """List 10 commits of a repo using GitHub API"""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    try:
        with requests.get(url, auth=Basic_auth(repo, owner)) as response:
            response.raise_for_status()
            commits_list = response.json()
            # print(help(commits))

            for commit_obj in commits_list[0:10]:
                # print(commit_obj)
                sha = commit_obj['sha']
                author_name = commit_obj['commit']['author']['name']
                print("{}: {}".format(sha, author_name))
    except Exception as e:
        pass


if __name__ == "__main__":
    list_commits(sys.argv[1], sys.argv[2])
