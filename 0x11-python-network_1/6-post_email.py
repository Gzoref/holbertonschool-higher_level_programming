#!/usr/bin/python3
'''
That takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally
displays the body of the response.
'''

import requests
import sys

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], email)
    print('{}'.format(response.text))
