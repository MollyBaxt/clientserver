import socket
from base64 import b64decode

from utils.cryp import decrypt_data
import json
from time import sleep

IP = "127.0.0.1"
PORT = 1234
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

print("[STARTING] Server is starting.")
""" Staring a TCP socket. """
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
""" Bind the IP and PORT to the server. """
server.bind(ADDR)
""" Server is listening, i.e., server is now waiting for the client to connected. """
server.listen()
print("[LISTENING] Server is listening.")
while True:
    """ Server has accepted the connection from the client. """
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")
    """ Receiving the filename from the client. """
    filename = conn.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename: {filename}.")
    conn.send("Filename received.".encode(FORMAT))
    """ Receiving the file data from the client. """
    if "encrypted" in filename:
        data = conn.recv(SIZE).decode(FORMAT)
        print(data, type(data))
        encrypted = b64decode(data)
        print(type(encrypted))
        decrypted = decrypt_data(encrypted)
        print(type(decrypted), decrypted)
        msg = decrypted.decode()
        with open('received_data.txt', 'w') as file:
            file.write(msg)
        print(msg)
    print(f"[RECV] Receiving the file data.")
    conn.send("File data received".encode(FORMAT))
    """ Closing the file. """
    file.close()
    """ Closing the connection from the client. """
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")


def output(data):
    print("placeholder")
