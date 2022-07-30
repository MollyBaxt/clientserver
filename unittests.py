import unittest
from src.generators import generate_dict, generate_text
import json
from random import randint
from time import time


class MyTestCase(unittest.TestCase):
    def test_generators(self):
        dict_expected = generate_dict()
        self.assertTrue(dict_expected, dict)

        str_expected = generate_text()
        self.assertTrue(str_expected, str)

    def test_json(self):
        sent_dict = {
        "id": randint(1, 100),
        "timestamp": time(),
        "data": hash(str(randint(1, 100)))
        }
        expected_received_dict = {json.dumps(sent_dict)}
        self.assertNotEqual(sent_dict, expected_received_dict)


if __name__ == '__main__':
    unittest.main()
