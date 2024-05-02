import math
import random

def main():

    try:

        

        user_input = int(input("Please guess a number between 1 and 100: "))

        randomnum = random.randrange(0,100) #Random number generated between 0 and 100
        
        inputdif = abs(user_input - randomnum) #Get the difference between the user's input and the chosen number

        while user_input != randomnum: #Keep looping until the user gets the number that the program is thinking of

            if inputdif <= 5 and inputdif < 15: #If the distance is between these values, tell the user how close they are.
                print("Very Hot")
                user_input = int(input("Please guess a number between 1 and 100: "))
                inputdif = abs(user_input - randomnum)
            if inputdif > 5 and inputdif <= 15:
                print("Hot")
                user_input = int(input("Please guess a number between 1 and 100: "))
                inputdif = abs(user_input - randomnum)
            if inputdif > 15 and inputdif <= 25:
                print("Cool")
                user_input = int(input("Please guess a number between 1 and 100: "))
                inputdif = abs(user_input - randomnum)
            if inputdif > 25:
                print("Cold")
                user_input = int(input("Please guess a number between 1 and 100: "))
                inputdif = abs(user_input - randomnum)

        print(f"You got it! The number was {randomnum}")

    except ValueError: #Catch invalid user input
        print("That is not a valid number.")
        main()






main()