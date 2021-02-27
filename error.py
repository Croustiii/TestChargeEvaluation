class ZeroErrorException(Exception):

    def __init__(self):
        self.__message = 'number is 0'

    def message(self):
        print(self.__message)  

class NegativeErrorException(Exception):

    def __init__(self):
        self.__message = 'number is negative'
    
    def message(self):
        print(self.__message)   