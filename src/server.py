import socket
from Cryptodome.Cipher import AES

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
    filename = conn.recv(TCP_BUFFER).decode("utf-8")
    print(filename)
    print("[SERVER] Received Filename :", filename)
    data = conn.recv(TCP_BUFFER)  # Client sending cipher message

    if "encrypted" in filename:
        ciphertext = data
        print("Received Encrypted Message:", ciphertext)
        print()
        cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)  # AES encryption using EAX -Encrypt/authenticate/translate
        plaintext = cipher.decrypt(ciphertext)  # decryption of cipher message passed from client
        print("Decrypting using Shared Key...")
        print(plaintext)
        print("data:", data)
    if "plaintext" in filename:
        plaintext = data
        print("Received Message:", plaintext)
        print("data:", data)
    if "json" in filename:
        print(data)

    break

print("Goodbye!")
tcp_server.close()
