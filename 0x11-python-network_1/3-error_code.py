#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request, parse, error
import sys

if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: {}'.format(e.code))
