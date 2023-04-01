#!/usr/bin/python3
'''This script takes in a letter as a parameter and sends a POST to a URL
'''
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        print('No result')
    else:
        if sys.argv[1] >= 'a' and sys.argv[1] <= 'z':
            data = {'q': sys.argv[1]}
        else:
            data = {'q': ''}
        if not data['q']:
            print('No result')
        else:
            response = requests.post(url, data)
            try:
                json = response.json()
                print('[{}] {}'.format(json.get('id'), json.get('name')))
            except Exception:
                print('Not a valid JSON')
