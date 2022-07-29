from src.generators import generate_dict, generate_text
from src.client import run_client
import json


def generate_data(sel):
    """Handle control flow of program based on user selection"""
    if sel == 1:
        msg = generate_text()
        run_client("plaintext", msg, False)
    elif sel == 2:
        msg = generate_text()
        run_client("encrypted", msg, True)
    else:
        data = json.dumps(generate_dict())
        run_client("json_data", data, False)







