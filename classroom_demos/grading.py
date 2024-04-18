class InvalidInputError(Exception):
    pass


def input_number():
    while True:
        try:
            user_input = int(input("Please enter a number:  "))
            return user_input

        except ValueError:
            print("Invalid input! Please enter a valid number.")

        else:
            return number


try:
    number = input_number()
    print("You have entered a valid number:  ", number)

finally:
    print("End of running configuration.")
