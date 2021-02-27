
from fizzBuzz import *
from error import *

def main() :
    try :
        number = input("Donnez moi un nombre !")
        print(FizzBuzz.Respond(int(number)))
    except Exception as e :
        e.message()

# Main
if __name__ == "__main__":
    main()



