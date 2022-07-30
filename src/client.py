import socket
from Cryptodome.Cipher import AES
from time import sleep

SERVER_IP = "127.0.0.1"  # Server IP of 127.0.0.1 LOOPBACK used for testing
SERVER_PORT = 9000  # Server Port
CIPHER_KEY = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'  # Encryption/decryption Key
NONCE = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'  # Shared NONCE key for validity


def encrypt(msg):
    """Func to encrypted text and return"""
    raw_message = msg.encode()  # Encode message to bytes
    CIPHER = AES.new(CIPHER_KEY, AES.MODE_EAX,
                     NONCE)  # Encryption using EAX with CIPHER and NONCE key
    ciphertext, tag = CIPHER.encrypt_and_digest(raw_message)
    return ciphertext


def run_client(filename, msg, do_encrypt):
    """Client checks for encryption, encodes to bytes and sends to server"""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
    client.connect((SERVER_IP, SERVER_PORT))  # TCP connection

    while True:
        raw_filename = filename.encode()
        print(f"[CLIENT] Sending filename: {filename}")
        client.send(raw_filename)
        sleep(0.01)  # Filename packet to be sent before sending data packet
        if do_encrypt:  # If do_encrypt is True, then pass data to be encrypted
            msg_packet = encrypt(msg)
        else:
            msg_packet = msg.encode()

        print(f"Sending Message: {msg_packet}")
        client.send(msg_packet)  # Send ciphertext of raw message
        break

    client.close()
    print('Message Sent..Closing')
    print()
