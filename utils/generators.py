from random import randint
from time import time
from utils.crypto import encrypt_data
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

    with open('data/lorem_plaintext.txt', 'w') as f:
        f.write(t)
        f.close()

    return 'lorem_plaintext.txt'


def generate_crytpo_text():
    t = encrypt_data(lorem.sentence())
    print(t)

    print(f"Text Generated:\n"
          f"{t}")

    with open('data/lorem_encrypted.txt', 'w') as f:
        f.write(str(t))
        f.close()

    return 'lorem_encrypted.txt'
