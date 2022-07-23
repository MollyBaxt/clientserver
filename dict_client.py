import socket
import sys
import json
from data import a_dict

jsonResult = json.dumps(a_dict)
try:
    sock = socket.socket()
except socket.error as err:
    print('Socket error because of %s' % err)

port = 11111
host = "localhost"

try:
    sock.connect((host, port))
    sock.send(bytes(jsonResult, 'utf-8'))
except socket.gaierror:

    print('There an error resolving the host')

    sys.exit()

print(jsonResult, 'was sent!')
sock.close()
