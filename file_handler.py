from generators import generate_dict, generate_plaintext, generate_crytpo_text
from n_client import client_textfile, client_connection
import json


def generate_data(sel):

    if sel == 1:
        file_name = generate_plaintext()
        client_textfile(file_name)
    elif sel == 2:
        file_name = generate_crytpo_text()
        client_textfile(file_name)
    else:
        data = json.dumps(generate_dict())
        client_connection(data)







