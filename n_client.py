import socket
import sys


def client_textfile(file_name):
    file = open(f"{file_name}.txt", "r")
    data = file.read()
    client_connection(data)


def client_connection(data):

    try:
        sock = socket.socket()
    except socket.error as err:
        print('Socket error because of %s' % err)

    port = 11111
    host = "localhost"

    try:
        sock.connect((host, port))
        sock.send(bytes(data, 'utf-8'))
    except socket.gaierror:

        print('There an error resolving the host')

        sys.exit()

    print(data, 'was sent!')
    sock.close()
