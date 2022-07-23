import socket
import sys
import json
from data import a_dict

json_result = json.dumps(a_dict)
try:
    sock = socket.socket()
except socket.error as err:
    print('Socket error because of %s' % err)

port = 11111
host = "localhost"

try:
    sock.connect((host, port))
    sock.send(bytes(json_result, 'utf-8'))
except socket.gaierror:

    print('There an error resolving the host')

    sys.exit()

print(json_result, 'was sent!')
sock.close()
