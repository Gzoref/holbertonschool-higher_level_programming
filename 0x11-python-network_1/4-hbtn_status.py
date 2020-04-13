#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
import requests

url = requests.get('https://intranet.hbtn.io/status')
print('Body response:')
print('\t- type: {}'.format(type(url.text)))
if url.status_code == 200:
    print('\t- content: OK')
