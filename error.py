class ZeroErrorException(Exception):

    def __init__(self):
        self.__message = 'number is 0'


class NegativeErrorException(Exception):

    def __init__(self):
        self.__message = 'number is negative'