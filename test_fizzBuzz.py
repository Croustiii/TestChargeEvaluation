import unittest
from fizzBuzz import *

class FizzBuzzTest(unittest.TestCase):
    #Test Part Rule Multiple of 3
    def test_should_be_Fizz_with_input_6(self):
        expected = 'Fizz'
        actual = FizzBuzz.Respond(6)
        self.assertEqual(actual, expected)


    def test_should_not_be_Fizz_with_input_10(self):
        expected = False
        actual = FizzBuzz.Respond(10)
        self.assertEqual(actual, expected)
    
    def test_should_be_Fizz_with_multiple_of_3_with_input_9(self):
        expected = 'Fizz'
        actual = FizzBuzz.Respond(9)
        self.assertEqual(actual, expected)
    

    #Test part Multiple of 5
    def test_should_be_Buzz_with_input_5(self):
        expected = 'Buzz'
        actual = FizzBuzz.Respond(5)
        self.assertEqual(actual, expected)