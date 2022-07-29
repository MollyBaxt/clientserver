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
print("[SERVER] Listening...")
conn, addr = tcp_server.accept()  # connection
print(f"Client Connected From: {addr}\n")


def output_result(data):
    """Ask if user wanted to output data to console."""
    to_output = input("Decrypted. Output? [Y/n]: ")
    if to_output == "y" or "Y":
        print(f" Decrypted Message is: {data}")


def export_to_file(filename, data):
    """Ask if user wanted to output data to file."""
    to_export = input("Export to file? [Y/n]: ")
    if to_export == "y" or "Y":
        with open(f"{filename}.txt", "w") as file:
            file.write(data)
            file.close()


while True:
    print("[SERVER] Receiving Message...")  # Prompt that message being received from client
    print()
    filename = conn.recv(TCP_BUFFER).decode()  # Decode filename from bytes to str
    print(filename)
    print(f"[SERVER] Received Filename: {filename}")
    sleep(0.1)
    data = conn.recv(TCP_BUFFER)  # Client sending message

    if "json" in filename:
        output_result(json.loads(data))  # Convert back to dict

    if "encrypted" in filename:
        ciphertext = data
        print("[SERVER] Received Encrypted Message:", ciphertext)
        cipher = AES.new(CIPHER_KEY, AES.MODE_EAX, NONCE)  # AES encryption using EAX -Encrypt/authenticate/translate
        plaintext = cipher.decrypt(ciphertext)  # decryption of cipher message passed from client
        print("[SERVER] Decrypting using Shared Key...")
        output_result(plaintext.decode())  # Send to out func
        export_to_file(filename, plaintext.decode())  # Send to export func

    if "plaintext" in filename:
        output_result(data.decode())
        export_to_file(filename, data.decode())

    break

print("Goodbye!")
tcp_server.close()  # Close server connection
