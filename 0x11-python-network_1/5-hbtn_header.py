#!/usr/bin/python3
'''
Takes in a URL, sends a request to the URL and displays the value of the
variable X-Request-Id in the response header
'''

import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
