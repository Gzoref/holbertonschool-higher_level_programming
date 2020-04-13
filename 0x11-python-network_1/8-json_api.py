#!/usr/bin/python3
'''
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

import requests
import sys

if __name__ == "__main__":
    url = 'http://b413be80f23b.44.hbtn-cod.io:5000'
    arg_length = len(sys.argv[1])
    if arg_length > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        req = r.json
        if not req:
            print('No result')
        else:
            print('[{}] {}'.format(req.get('id'), req.get('name')))
    except ValueError:
        print('Not a valid JSON')
