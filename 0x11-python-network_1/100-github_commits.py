#!/usr/bin/python3
'''List 10 commits (from the most recent to oldest) of the repository “rails”
    by the user “rails”. You must use the GitHub API, here is the
    documentation https://developer.github.com/v3/repos/commits/
    Print all commits by: `<sha>: <author name>` (one by line)
'''
import sys
import requests

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    for commit in response.json()[:10]:
        print('{}: {}'.format(
            commit.get('sha'), commit.get('commit').get('author').get('name')))
