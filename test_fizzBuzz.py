import unittest
from fizzBuzz import *
from error import ZeroErrorException

class FizzBuzzTest(unittest.TestCase):
    #Test Part Rule Multiple of 3
    def test_should_be_Fizz_with_input_6(self):
        expected = 'Fizz'
        actual = FizzBuzz.Respond(6)
        self.assertEqual(actual, expected)


    def test_should_not_be_Fizz_with_input_11(self):
        expected = False
        actual = FizzBuzz.Respond(11)
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
    
    def test_should_not_be_Buzz_with_input_7(self):
        expected = False
        actual = FizzBuzz.Respond(7)
        self.assertEqual(actual, expected)


    #Test part Multiple of 3 and 5
    def test_should_be_FizzBuzz_with_multiple_of_3_and_5_with_input_15(self):
        expected = 'FizzBuzz'
        actual = FizzBuzz.Respond(15)
        self.assertEqual(actual, expected)

    def test_should_be_FizzBuzz_with_multiple_of_3_and_5_with_input_30(self):
        expected = 'FizzBuzz'
        actual = FizzBuzz.Respond(30)
        self.assertEqual(actual, expected)

    # Test input 0 exception raised
    def test_should_raise_exception_with_input_0(self):
        with self.assertRaises(ZeroErrorException):
            FizzBuzz.Respond(0)

    
    # Test input 0 exception raised
    def test_should_raise_exception_with_input_negative(self):
        with self.assertRaises(NegativeErrorException):
            FizzBuzz.Respond(-5)
