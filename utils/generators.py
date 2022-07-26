from random import randint
from time import time
from utils.cryp import generate_secret_key, encrypt_data
from base64 import b64encode
import lorem


def generate_dict():
    # """Generate random json packet with hashed data bits"""
    return {
        "id": randint(1, 100),
        "timestamp": time(),
        "data": hash(str(randint(1, 100)))
    }


def generate_plaintext():
    t = lorem.sentence()
    print(f"Text Generated:\n"
          f"{t}")

    with open('lorem_plaintext.txt', 'w') as f:
        f.write(t)
        f.close()

    return 'lorem_plaintext.txt'


def generate_crytpo_text():
    key = generate_secret_key()
    msg = lorem.sentence()
    enc_msg = encrypt_data(msg, key, "{")
    print(f"Type is {type(enc_msg)}")
    print(f"Text Generated:\n"
          f"{enc_msg}")

    with open('lorem_encrypted.txt', 'w') as f:
        f.write(enc_msg)
        f.close()

    return 'lorem_encrypted.txt'

