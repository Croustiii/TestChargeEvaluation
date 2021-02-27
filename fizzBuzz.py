from error import *
class FizzBuzz:
    @staticmethod
    def Respond(number):
        if isinstance(number, (int,float)):
            if (number == 0):
                raise ZeroErrorException()
            if (number < 0):
                raise NegativeErrorException()            
            if (number % 3 == 0 and number % 5 == 0):
                return 'FizzBuzz'
            if (number % 3 == 0):
                return 'Fizz'
            if (number  % 5 == 0):
                return 'Buzz'
            return number
        raise NotNumberErrorException()