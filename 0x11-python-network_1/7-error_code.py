#!/usr/bin/python3
'''Send a request to a URL, passed as an argument,
    and display the response body
'''
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code < 400:
        print(response.text)
    else:
        print('Error code:', response.status_code)
