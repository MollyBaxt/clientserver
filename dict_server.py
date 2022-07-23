import socket

sock = socket.socket()
print("Socket created ...")

host = 'localhost'
port = 11111
sock.bind((host, port))
sock.listen(5)

print('socket is listening')

while True:
    c, addr = sock.accept()
    print('got connection from ', addr)

    jsonReceived = c.recv(1024)
    print("Json received -->", jsonReceived)

    c.close()
