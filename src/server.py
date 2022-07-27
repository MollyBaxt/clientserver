import socket
from Cryptodome.Cipher import AES
import json
from time import sleep

SERVER_IP = "127.0.0.1"  # Server IP using Loopback for testing
SERVER_PORT = 9000  # Server Port
CIPHER_KEY = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'  # Shared Key 32 bytes for 256-bit encryption
TCP_BUFFER = 1024  # Buffer for receiving data
NONCE = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'  # shared nonce key for validation.

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # initialize TCP stream
tcp_server.bind((SERVER_IP, SERVER_PORT))  # Bind TCP Stream connection
tcp_server.listen(1)  # Listen for TCP connection

conn, addr = tcp_server.accept()  # connection
print('Client Connected From:', addr)
print()

while True:
    print("[SERVER] Receiving Message...")
    print()
    filename = conn.recv(TCP_BUFFER).decode()
    print(filename)
    print("[SERVER] Received Filename :", filename)
    sleep(0.1)
    data = conn.recv(TCP_BUFFER) # Client sending message

    if "json" in filename:
        print(f"[SERVER] {json.loads(data)}")
    if "encrypted" in filename:
        ciphertext = data
        print("[SERVER] Received Encrypted Message:", ciphertext)
        cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)  # AES encryption using EAX -Encrypt/authenticate/translate
        plaintext = cipher.decrypt(ciphertext)  # decryption of cipher message passed from client
        print("[SERVER] Decrypting using Shared Key...")
        print(plaintext.decode())
    if "plaintext" in filename:
        print(data.decode())

    break

print("Goodbye!")
tcp_server.close()
