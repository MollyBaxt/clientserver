#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = "localhost"
print(host)                # Get local machine name
port = 1233                # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024))
s.close()                     # Close the socket when done