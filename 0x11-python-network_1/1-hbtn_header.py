#!/usr/bin/python3
'''
Script that fetches https://intranet.hbtn.io/status
'''
from urllib import request
import sys

url = sys.argv[1]
with request.urlopen(url) as response:
    print(response.getheader('X-Request-Id'))
