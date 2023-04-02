import unittest
from vingere import *


class TestVingereCiphr(unittest.TestCase):

    def setUp(self) -> None:
        self.cipher = VigenereCipher("TRAIN")

    def test_encode(self):
        encoded = self.cipher.encode("ENCODEDINPYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_character(self):
        encoded = self.cipher.encode("E")
        self.assertEqual(encoded, "X")

    def test_encode_spaces(self):
        encoded = self.cipher.encode("ENCODED IN PYTHON")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_encode_lowercase(self):
        encoded = self.cipher.encode("encoded in Python")
        self.assertEqual(encoded, "XECWQXUIVCRKHWA")

    def test_combine_character(self):
        self.assertEqual(VigenereCipher.combine_character("E", "T"), "X")
        self.assertEqual(VigenereCipher.combine_character("N", "R"), "E")

    def test_extend_keyword(self):
        extended = self.cipher.extend_keyword(16)
        self.assertEqual(extended, "TRAINTRAINTRAINT")

    def test_separate_character(self):
        self.assertEqual(VigenereCipher.separate_character("X", "T"), "E")
        self.assertEqual(VigenereCipher.separate_character("E", "R"), "N")


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
