#!/usr/bin/python3
"""I documented you"""

<<<<<<< HEAD
import urllib.request
=======
mport urllib.request
>>>>>>> 1dec73146b60274cd3d86ed2d8ae604b758150bc
import urllib.parse
import sys

if __name__ == '__main__':
    """"Documented"""
    url = sys.argv[1]
    message = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(message)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
