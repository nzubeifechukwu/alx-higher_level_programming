#!/usr/bin/python3
'''Send a request to a URL passed as an argument and display the value of the
    X-Request-Id variable found in the response header
'''
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) as response:
        pass
    print(response.headers.get('X-Request-Id'))
