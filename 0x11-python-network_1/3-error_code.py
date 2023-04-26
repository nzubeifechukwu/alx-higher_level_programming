#!/usr/bin/python3
'''Send a request to a URL, passed as an argument, and display the
    response of the body (decoded in utf-8)
'''
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as response:
            page = response.read()
    except HTTPError as e:
        print('Error code:', e.code)
    else:
        print(page.decode())
