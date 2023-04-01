#!/usr/bin/python3
'''Send a POST request to a URL (passed as a parameter), with an email as a
    parameter, and display the body of the response (decoded in utf-8)
'''
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        page = response.read()

    print(page.decode())
