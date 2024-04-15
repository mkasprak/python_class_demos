class InvalidInputError(ValueError):
    # Custom exception implementation
    print("Naughty naughty! You were not supposed to do that")


def main():
    try:
        value = int(input("Please enter a number between 0 and 9 "))
        print(f"You entered: {value}")

    except ValueError:
        print("Shame")
    except Exception as e:
        print(e.__str__)
        print("You need to input a whole number.")
        main()
    else:
        print("Thank you for entering a valid number.")
    finally:
        print("Thank's for playing!")


main()
