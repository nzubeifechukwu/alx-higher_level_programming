#!/usr/bin/python3
'''Send a request to a URL, passed as an argument, and display the value of
    the X-Request-Id variable of the response header
'''
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers.get('X-Request-Id'))
