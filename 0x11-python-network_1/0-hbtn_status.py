#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request

url = 'https://intranet.hbtn.io/status'
with request.urlopen(url) as response:
    the_page = response.read()
    print('Body response:')
    print('- type: {}'.format(type(the_page)))
    print('- content: {}'.format(the_page))
    print('- utf8 content: {}'.format(the_page.decode('utf-8')))
