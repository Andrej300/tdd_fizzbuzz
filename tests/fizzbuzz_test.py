import unittest
from src.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizzbuzz_3_return_fizz(self):
        self.assertEqual("fizz", fizzbuzz(3))

    def test_fizzbuzz_5_return_buzz(self):
        self.assertEqual("buzz", fizzbuzz(5))

    def test_fizzbuzz_15_return_buzz(self):
        self.assertEqual("fizzbuzz", fizzbuzz(15))

    def test_fizzbuzz_4_return_4_as_str(self):
        self.assertEqual("4", fizzbuzz(4))

    def test_fizzbuzz_90_return_fizzbuzz(self):
        self.assertEqual("fizzbuzz", fizzbuzz(90))

# THE TESTS PASSED SUCCESFULLY
