import unittest
from fizzBuzz import *

class FizzBuzzTest(unittest.TestCase):
    
    def test_should_be_Fizz_with_input_6(self):
        expected = 'Fizz'
        actual = FizzBuzz.Respond(6)
        self.assertEqual(actual, expected)