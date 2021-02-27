
from fizzBuzz import *
from error import *

def main() :
    try :
        number = input("Donnez moi un nombre !")
        numInt = int(number)
        print(FizzBuzz.Respond(numInt))
    except Exception as e :
        e.message()

# Main
if __name__ == "__main__":
    main()



