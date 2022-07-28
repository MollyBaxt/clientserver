from random import randint
from time import time
import lorem


def generate_dict():
    # """Generate random json packet with hashed data bits"""
    return {
        "id": randint(1, 100),
        "timestamp": time(),
        "data": hash(str(randint(1, 100)))
    }


def generate_text():
    text = lorem.sentence().strip(".")

    with open("some_text.txt", "w") as file:
        file.write(text)
        file.close()

    return text


