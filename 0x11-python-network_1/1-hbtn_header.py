#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request
import sys

with request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
