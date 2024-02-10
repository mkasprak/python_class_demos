import random


def main():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != target_number:
        # Get user's guess
        try:
            guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Calculate the difference
        difference = abs(guess - target_number)

        # Provide feedback
        if difference == 0:
            print(
                f"Congratulations! You've guessed the right number in {attempts} attempts.")
        elif difference <= 5:
            print("Very Hot")
        elif difference <= 15:
            print("Hot")
        elif difference <= 25:
            print("Cool")
        else:
            print("Cold")


main()
