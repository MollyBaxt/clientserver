import unittest
from src.generators import generate_dict, generate_text


class MyTestCase(unittest.TestCase):
    def test_generators(self):
        dict_expected = generate_dict()
        self.assertTrue(dict_expected, dict)

        str_expected = generate_text()
        self.assertTrue(str_expected, str)


if __name__ == '__main__':
    unittest.main()
