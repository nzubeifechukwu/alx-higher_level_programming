#!/usr/bin/python3
'''Fetch a url using the requests package
'''
import requests

if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type:', type(req.text))
    print('\t- content:', req.text)
