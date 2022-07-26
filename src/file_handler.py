from generators import generate_dict, generate_text
from client import run_client
import json


def generate_data(sel):

    if sel == 1:
        msg = generate_text()
        run_client("plaintext", msg, False)
    elif sel == 2:
        msg = generate_text()
        run_client("encrypted", msg, True)
    else:
        data = json.dumps(generate_dict())
        run_client("json_data", data, False)







