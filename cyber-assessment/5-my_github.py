#!/usr/bin/python3
import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

r = requests.get('https://api.github.com/user', auth=(username, password))

if r.status_code == 200:
    print(r.json()['id'])
else:
    print(None)
