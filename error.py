class ZeroErrorException(Exception):

    def __init__(self):
        self.__message = 'le nombre est 0'
    