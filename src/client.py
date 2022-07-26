import socket
from Cryptodome.Cipher import AES

SERVER_IP = "127.0.0.1"  # server IP of 127.0.0.1 LOOPBACK used for testing
SERVER_PORT = 9000  # server Port
CIPHER_KEY = b'bQeThWmZq4t7w!z%C*F-JaNdRfUjXn2r'  # Shared Encryption/decryption Key
NONCE = b'dRgUkXp2s5v8y/B?E(G+KbPeShVmYq3t'  # shared NONCE key for validity


def encrypt(msg):
    raw_message = msg.encode("utf-8")  # Encode message to bytes
    CIPHER = AES.new(CIPHER_KEY, AES.MODE_EAX,
                     NONCE)  # AES encryption using EAX  with predefined cipher key and nonce key for validation
    ciphertext, tag = CIPHER.encrypt_and_digest(raw_message)
    return ciphertext


def run_client(filename, msg, do_encrypt):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket creation
    client.connect((SERVER_IP, SERVER_PORT))  # TCP connection

    while True:
        raw_filename = filename.encode("utf-8")
        client.send(raw_filename)
        print()
        raw_message = msg.encode("utf-8")  # Encode message to bytes
        print(raw_message)
        if do_encrypt:
            msg_packet = encrypt(msg)
            print(msg_packet)
        else:
            msg_packet = raw_message
            print(f"Not encrypted: {msg_packet}")
        print("Sending Message:", msg_packet)
        client.send(msg_packet)  # send ciphertext of raw message
        print()
        break

    client.close()
    print('Message Sent..Goodbye')
    print()


