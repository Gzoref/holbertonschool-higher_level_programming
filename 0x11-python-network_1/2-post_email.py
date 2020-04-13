#!/usr/bin/python3
'''
Script that sends a request to the URL and displays the body of the response
'''

from urllib import request, parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    values = parse.urlencode(values).encode('utf-8')
    req = request.Request(url, values)

    with request.urlopen(req) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
