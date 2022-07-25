import socket

IP = "127.0.0.1"
PORT = 1234
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def client_textfile(file_name):
    file = open(f"data/client_data/{file_name}", "r")
    data = file.read()
    client_connection(data)
    file.close()


def client_connection(file_name, data):
    print(file_name, data)
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    """ Connecting to the server. """
    client.connect(ADDR)
    """ Sending the filename to the server. """
    client.send(file_name.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    """ Sending the file data to the server. """
    client.send(data.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")
    """ Closing the file. """
    """ Closing the connection from the server. """
    client.close()

